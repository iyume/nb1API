"""
the tool box for solving the document.

this module should be injected to the Mako render context.

Solution:

    `Description`:
        Any docstring (include variable comment) will be parsed to
        short_description and long_description,
        and a normal_description give f'{shot_desc}\\n\\n{long_desc}'

    `other similar block`:
        normally list of `name(annot) <badge>: desc`
"""
from typing import Union, Optional, Callable, List, Tuple, Type
import re
import inspect
from textwrap import dedent
from dataclasses import dataclass

import pdoc
from pdoc.pycode import formatannotation


T_Annotation = Optional[str]
T_Version = Optional[str]
T_Description = Optional[str]


@dataclass
class DocstringParam:
    """ dataclass for `args` and `attributes` or other similar block """
    name: str
    annotation: T_Annotation = None
    version: T_Version = None  # third-level version
    # default: Optional[str] = None  ## default value has been described in title
    description: T_Description = ''


@dataclass
class DocstringSection:
    identity: str
    # empty when content parsed to nothing, that directly render source
    content: List[DocstringParam]
    source: str = ''
    version: T_Version = None  # second-level version
    def __str__(self):
        return self.source


class Docstring:
    """
    NOTE:
        When long_description include `\n`, a short_description is required,
        or the first line of long_description will be thinked as short_description.
    """
    _sections = {
        "args": { "Arguments", "Args", "Parameters", "Params", "参数" },
        "returns": { "Return", "Returns", "返回" },
        "attributes": { "Attributes", "属性" },  # add it in class's docstring
        "raises": { "Raises", "Exceptions", "Except", "异常" },
        "examples": { "Example", "Examples", "示例", "用法" },
        "require": { "Require", "要求" },
        "version": { "Version", "版本" },
        "type_version": { "TypeVersion", "类型版本" }
    }
    __slots__ = ('short_desc', 'long_desc', 'description', 'var_type',
                *(i for i in _sections))
    title_re = re.compile(
        "^("
        + "|".join({sec for _ in _sections.values() for sec in _})
        + r")(?:\((.*?)\))?:",
        flags=re.M
    )

    short_desc: str
    long_desc: str
    description: str
    type_version: str  # special in variable docstring
    args: DocstringSection
    returns: DocstringSection
    attributes: DocstringSection
    raises: DocstringSection
    examples: DocstringSection
    require: DocstringSection
    version: T_Version  # top-level version

    def __init__(self, **kwargs) -> None:
        self.short_desc = ''
        self.long_desc = ''
        self.description = ''

    def parse(self, text: str) -> None:
        if not text:
            return
        text = inspect.cleandoc(text)
        matches = list(self.title_re.finditer(text))
        desc_chunk = text[:matches[0].start()] if matches else text
        desc_chunk = desc_chunk.strip()
        desc_parts = [i.strip() for i in desc_chunk.split('\n', 1)]
        self.short_desc = self.description = desc_parts[0]
        if len(desc_parts) == 2:
            self.long_desc = desc_parts[1]
            self.description += f'\n\n{self.long_desc}'
        if not matches:
            return
        splits: List[Tuple[str, slice]] = []  # raw text sections
        for i in range(len(matches) - 1):
            splits.append((matches[i].group(1), slice(matches[i].end(), matches[i + 1].start())))
        splits.append((matches[-1].group(1), slice(matches[-1].end(), None)))
        for i, (name, seg) in enumerate(splits):
            for identity, set_ in self._sections.items():
                if not name in set_:
                    continue
                text_sec = dedent(text[seg]).strip()
                section = DocstringSection(identity=identity,
                        version=matches[i].group(2), content=[], source=text_sec)
                # try to call self-defined method
                method_str = 'parse_' + identity
                method = getattr(self, method_str, None)
                if method is not None and callable(method):
                    try:
                        method(section)
                    except Exception:
                        print('ERROR parsing docstring:',
                            f'Find method `{method.__name__}` but raises when calling.')
                    continue
                # setattr to string if anno is not DocstringSection
                if not self.__annotations__.get(identity, None) is DocstringSection:
                    setattr(self, identity, text_sec)
                    continue
                self.generic_parser(section)

    @staticmethod
    def _parse_params(s: str) -> List[DocstringParam]:
        """
        Example:
            ```
            arg1(1.1.0+): desc1
            arg2: this is a long long,
                    long description.
            ```
            will produce
            ```
            List[
                DocstringParam(name="arg1", annotation=None,
                    version="1.1.0+", description="desc1"),
                DocstringParam(name="arg2", annotation=None,
                    version=None, description="this is a long long, long description")
            ]
            ```
        """
        result: List[DocstringParam] = []
        matches = list(re.finditer(r'^([a-zA-Z0-9_]+) ?(?:\((.*?)\))?:', s, flags=re.M))
        if not matches:
            return []
        splits: List[Tuple[str, str]] = []
        for i in range(len(matches) - 1):
            splits.append((matches[i].group(1), s[matches[i].end():matches[i + 1].start()]))
        splits.append((matches[-1].group(1), s[matches[-1].end():]))
        for i, (arg_name, desc) in enumerate(splits):
            result.append(DocstringParam(
                name=arg_name,
                version=matches[i].group(2),
                description=re.sub(r'\n[ ]*', ' ', desc).strip()
            ))
        return result

    def generic_parser(self, section: DocstringSection) -> None:
        """
        try to parse the content in each section, or leave it str.
        if you want to control a special section, write method in form of `parse_` + `identity`.
        """
        text = section.source
        if not isinstance(text, str):
            return
        params = self._parse_params(text)
        if params:
            section.content = params
        setattr(self, section.identity, section)

    def resolve(self, mod: pdoc.Doc, link: Callable = None) -> None:
        """
        resolve self to render powerful docstring.
        """
        if isinstance(mod, pdoc.Class):
            args_sec = DocstringSection(
                identity='args', content=get_func_params(mod.obj.__init__))
            if hasattr(self, 'args') and isinstance(self.args, DocstringSection):
                args_sec = self._resolve_params(args_sec, self.args)
            self.args = args_sec
        elif isinstance(mod, pdoc.Function):
            # reorganize `self.args` by sorting in order of `get_func_params`
            # and add annotation for param if annotation exists
            # resolve params
            args_sec = DocstringSection(
                identity='args', content=get_func_params(mod.obj))
            if hasattr(self, 'args') and isinstance(self.args, DocstringSection):
                args_sec = self._resolve_params(args_sec, self.args)
            self.args = args_sec
            # resolve returns when `Returns:` not write in docstring
            if not getattr(self, 'returns', None):
                return_anno = mod.return_annotation()
                if not return_anno:
                    return_anno = 'unknown'
                self.returns = DocstringSection(identity='returns', content=[], source=return_anno)
        elif isinstance(mod, pdoc.Variable):
            self.var_type = mod.type_annotation()

    @staticmethod
    def _resolve_params(sec1: DocstringSection, sec2: DocstringSection) -> DocstringSection:
        """
        merge `sec1` and `sec2`.

        `sec1` is auto-generated from source code, `sec2` is extracted from its docstring.
        """
        if sec2.version:
            sec1.version = sec2.version
        param_dict = {
            arg.name: (arg.version, arg.description)
            for arg in sec2.content
        }
        for p in sec1.content:
            p.version, p.description = param_dict.get(p.name, (None, ''))
        return sec1


def get_func_params(obj: Type, str: bool = False) -> List[DocstringParam]:
    """
    this function will be merge to pdoc module

    Args:
        str: return str from inspect.Parameter.__str__
    """
    signature = inspect.signature(obj)
    result: List[DocstringParam] = []
    for p in signature.parameters.values():
        if p.name == 'self':
            continue
        result.append(DocstringParam(
            name=p.name,
            annotation=formatannotation(p.annotation)))
    return result

def get_method_type(mod: pdoc.Function) -> str:
    """
    produce `classmethod async def` or `staticmethod async def`
    or simply just `def`
    """
    builder = []
    builder.append(mod.funcdef())
    if mod.cls is not None and not mod.is_method:
        # not a normal bound method will be `classmethod` or `staticmethod`
        mtype = pdoc.Class._method_type(mod.cls.obj, mod.name)
        builder.append('classmethod' if mtype is classmethod else 'staticmethod')
    return ' '.join(builder)

def get_title(mod: pdoc.Doc) -> str:
    """
    produce prefix like `_abstract classmethod async def_` for classmethod, 
    or `_abstract property_` for abstract property, 
    or `_abstract class_` for abstract class.
    produce body like `MyClass`, `MyDef(params)`
    """
    assert not isinstance(mod, pdoc.Module)

    def is_abstract(mod: pdoc.Doc) -> bool:
        assert not isinstance(mod, pdoc.Module)
        if isinstance(mod, pdoc.Class):
            return inspect.isabstract(mod.obj)
        if isinstance(mod, (pdoc.Function, pdoc.Variable)):
            if mod.cls is None:
                # function in module level is not abstract
                return False
            return mod.name in getattr(mod.cls.obj, '__abstractmethods__', [])
        return False
    def is_property(mod: pdoc.Doc) -> bool:
        # return isinstance(mod.obj, property)
        # isinstance not work due to pdoc take the `fget` object
        # rather than property itself
        return mod.source.startswith('@property')

    prefix_builder = []
    body = mod.name
    if is_abstract(mod):
        prefix_builder.append('abstract')
    if is_property(mod):
        prefix_builder.append('property')
    if isinstance(mod, pdoc.Class):
        prefix_builder.append('class')
        body += '(%s)' % ', '.join(mod.params(annotate=False))
    if isinstance(mod, pdoc.Function):
        prefix_builder.append(get_method_type(mod))
        body += '(%s)' % ', '.join(mod.params(annotate=False))
        # global config `show_type_annotations`
        # NOTE: ForwardRef is not resolve here, so `show_type_annotations` should be False
    if isinstance(mod, pdoc.Variable):
        if is_property(mod):
            pass
        elif mod.cls is None: # is module-level variable
            prefix_builder.append('var')
        else:
            prefix_builder.append('instance-var' if mod.instance_var else 'class-var')
    if isinstance(mod, pdoc.LibraryAttr):
        prefix_builder.append('library-attr')
    prefix = ' '.join(prefix_builder)
    return f'_{prefix}_ `{body}`'

def get_version(doc: Union[str, Docstring, DocstringSection, DocstringParam],
                                prefix: str = ' ',suffix: str = '') -> str:
    if isinstance(doc, str):
        version = doc
    else:
        version = getattr(doc, 'version', '')
    if not version:
        return ''
    s = '{}<Badge text="{}"/>{}'
    if version.endswith('-'):
        s = '{}<Badge text="{}" type="error"/>{}'
    return s.format(prefix, version, suffix)

def get_doc(mod: Union[str, pdoc.Doc]):
    doc = Docstring()
    docstring = mod if isinstance(mod, str) else mod.docstring
    doc.parse(docstring)
    if not isinstance(mod, (str, pdoc.LibraryAttr)):
        # Do not resolve for LibraryAttr
        doc.resolve(mod)
    return doc
