"""
Pick variable docstring from module-level and class-level.

Priority: `docstring` > `comment_ahead` > `comment_inline` > `comment_after`
`docstring` is ast.Expr after ast.Assign or ast.AnnAssign.
`comment_after` appear in one line after assignment.

Example:
    ```python
    #: connect
    #: comment ahead
    a = 1  #: comment inline
    #: comment after
    ```
    a's docstring is 'connect<newline>comment ahead'

    ```python
    #: comment ahead
    a = 1
    '''
    example docstring
    '''
    ```
    a's docstring is 'example docstring'
"""
from typing import Iterable, List, Dict, Tuple, Union, Optional, Any, cast
import ast
import re
import itertools
import inspect
from inspect import Signature
from collections import OrderedDict


comment_re = re.compile(r'^\s*#: ?(.*)$')
indent_re = re.compile(r'^\s*$')
emptyline_re = re.compile(r'^\s*(#.*)?$')


def extract_all_comments(source: str) -> 'VariableCommentPicker':
    picker = VariableCommentPicker(source.splitlines())
    astmodule = ast.parse(source)
    picker.visit(astmodule)
    return picker


def get_assign_targets(node: Union[ast.Assign, ast.AnnAssign]) -> List[ast.expr]:
    """
    An AnnAssign `target` is a single node.
    An Assign `targets` is a list of nodes.

    Example:
        `a = b = 1` return [ast.Name('a'), ast.Name('b')]
        `a, b = c` return [ast.Tuple(('a', 'b'))]
    """
    if isinstance(node, ast.Assign):
        return node.targets
    else:
        return [node.target]


def get_target_names(node: Union[str, ast.AST],
                    self: Optional[ast.arg] = None) -> List[str]:
    """Convert assignment-AST to variable names.
    This raises `TypeError` if the assignment does not create new variable::
        ary[0] = 'foo'
        dic["bar"] = 'baz'
        # => TypeError

    Args:
        node: the `target` in ast.Assign
    """
    if isinstance(node, str):
        return [node]
    node_name = node.__class__.__name__
    if node_name in ('Index', 'Num', 'Slice', 'Str', 'Subscript'):
        raise TypeError('%r does not create new variable' % node)
    elif node_name == 'Name':
        node = cast(ast.Name, node)
        if self is None or node.id == self.arg:
            return [node.id]
        else:
            raise TypeError('The assignment %r is not instance variable' % node)
    elif node_name in ('Tuple', 'List'):
        node = cast(Union[ast.Tuple, ast.List], node)
        members = []
        for elt in node.elts:
            try:
                members.extend(get_target_names(elt, self))
            except TypeError:
                pass
        return members
    elif node_name == 'Attribute':
        node = cast(ast.Attribute, node)
        if (node.value.__class__.__name__ == 'Name' and self and
                cast(ast.Name, node.value).id == self.arg):
            # instance variable
            return [node.attr]
        else:
            raise TypeError('The assignment %r is not instance variable' % node)
    else:
        raise NotImplementedError('Unexpected node name %r' % node_name)


def dedent_docstring(s: str) -> str:
    """Remove common leading indentation from docstring."""
    def dummy() -> None:
        # dummy function to mock `inspect.getdoc`.
        pass

    dummy.__doc__ = s
    docstring = inspect.getdoc(dummy)
    if docstring:
        return docstring.lstrip("\r\n").rstrip("\r\n")
    else:
        return ""


class VariableCommentPicker(ast.NodeVisitor):
    """Python source code parser to pick up variable comments."""

    def __init__(self, buffers: Iterable[str], encoding: str = 'utf-8') -> None:
        self.counter = itertools.count()
        self.buffers = list(buffers)
        self.encoding = encoding
        self.context: List[str] = []
        self.current_classes: List[str] = []
        self.current_function: Optional[ast.FunctionDef] = None
        self.comments: Dict[str, str] = OrderedDict()
        self.previous: Optional[ast.AST] = None
        self.deforders: Dict[str, int] = {}
        self.finals: List[str] = []
        self.overloads: Dict[str, List[Signature]] = {}
        self.typing: Optional[str] = None
        self.typing_final: Optional[str] = None
        self.typing_overload: Optional[str] = None
        super().__init__()

    def get_qualname_for(self, name: str) -> Optional[List[str]]:
        """Get qualified name for given object as a list of string(s)."""
        if self.current_function:
            if self.current_classes and self.context[-1] == "__init__":
                # store variable comments inside __init__ method of a class
                return self.context[:-1] + [name]
            else:
                return None
        else:
            return self.context + [name]

    def add_entry(self, name: str) -> None:
        qualname = self.get_qualname_for(name)
        if qualname:
            self.deforders[".".join(qualname)] = next(self.counter)

    def add_final_entry(self, name: str) -> None:
        qualname = self.get_qualname_for(name)
        if qualname:
            self.finals.append(".".join(qualname))

    def add_overload_entry(self, func: ast.FunctionDef) -> None:
        # avoid circular import problem
        qualname = self.get_qualname_for(func.name)
        if qualname:
            overloads = self.overloads.setdefault(".".join(qualname), [])

    def add_variable_comment(self, name: str, comment: str) -> None:
        qualname = self.get_qualname_for(name)
        if qualname:
            basename = ".".join(qualname[:-1])
            if basename:
                name = ".".join((basename, name))
            self.comments[name] = comment

    def is_final(self, decorators: List[ast.expr]) -> bool:
        final = []
        if self.typing:
            final.append('%s.final' % self.typing)
        if self.typing_final:
            final.append(self.typing_final)

        for decorator in decorators:
            try:
                if ast.unparse(decorator) in final:
                    return True
            except NotImplementedError:
                pass

        return False

    def is_overload(self, decorators: List[ast.expr]) -> bool:
        overload = []
        if self.typing:
            overload.append('%s.overload' % self.typing)
        if self.typing_overload:
            overload.append(self.typing_overload)

        for decorator in decorators:
            try:
                if ast.unparse(decorator) in overload:
                    return True
            except NotImplementedError:
                pass

        return False

    def get_self(self) -> Optional[ast.arg]:
        """Returns the name of the first argument if in a function."""
        if self.current_function and self.current_function.args.args:
            return self.current_function.args.args[0]
        else:
            return None

    def get_line(self, lineno: int) -> str:
        """Returns specified line."""
        return self.buffers[lineno - 1]

    def visit(self, node: ast.AST) -> None:
        """Updates self.previous to the given node."""
        super().visit(node)
        self.previous = node

    def visit_Import(self, node: ast.Import) -> None:
        """Handles Import node and record the order of definitions."""
        for name in node.names:
            self.add_entry(name.asname or name.name)
            if name.name == 'typing':
                self.typing = name.asname or name.name
            elif name.name == 'typing.final':
                self.typing_final = name.asname or name.name
            elif name.name == 'typing.overload':
                self.typing_overload = name.asname or name.name

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Handles Import node and record the order of definitions."""
        for name in node.names:
            self.add_entry(name.asname or name.name)
            if node.module == 'typing' and name.name == 'final':
                self.typing_final = name.asname or name.name
            elif node.module == 'typing' and name.name == 'overload':
                self.typing_overload = name.asname or name.name

    def visit_Assign(self, node: ast.Assign) -> None:
        """Handles Assign node and pick up a variable comment."""
        try:
            targets = get_assign_targets(node)
            varnames: List[str] = sum([get_target_names(t, self=self.get_self()) for t in targets], [])  # NOQA
            current_line = self.get_line(node.lineno)
        except TypeError:
            return  # this assignment is not new definition!

        comment: Optional[str] = None

        if indent_re.match(current_line[:node.col_offset]):

            # check comments after assignment
            current_line_ext = current_line[node.end_col_offset:]
            current_line_after = self.get_line(node.lineno + 1)
            if comment_re.match(current_line_after):
                comment = comment_re.sub(r'\1', current_line_after)
            elif comment_re.match(current_line_ext):
                comment = comment_re.sub(r'\1', current_line_ext)

            # check comments before assignment
            comment_lines = []
            for i in range(node.lineno - 1):
                before_line = self.get_line(node.lineno - 1 - i)
                if comment_re.match(before_line):
                    comment_lines.append(comment_re.sub(r'\1', before_line))
                else:
                    break
            if comment_lines:
                comment = '\n'.join(reversed(comment_lines))

        if comment is not None:
            for varname in varnames:
                self.add_variable_comment(varname, comment)
            return

        # not commented (record deforders only)
        for varname in varnames:
            self.add_entry(varname)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        """Handles AnnAssign node and pick up a variable comment."""
        self.visit_Assign(node)  # type: ignore

    def visit_Expr(self, node: ast.Expr) -> None:
        """Handles Expr node and pick up a comment if string."""
        if (isinstance(self.previous, (ast.Assign, ast.AnnAssign)) and
                isinstance(node.value, ast.Str)):
            try:
                targets = get_assign_targets(self.previous)
                varnames = get_target_names(targets[0], self.get_self())
                for varname in varnames:
                    if isinstance(node.value.s, str):
                        docstring = node.value.s
                    else:
                        docstring = node.value.s.decode(self.encoding or 'utf-8')

                    self.add_variable_comment(varname, dedent_docstring(docstring))
                    self.add_entry(varname)
            except TypeError:
                pass  # this assignment is not new definition!

    def visit_Try(self, node: ast.Try) -> None:
        """Handles Try node and processes body and else-clause.
        This special visitor ignores objects definition in except-clause.
        """
        for subnode in node.body:
            self.visit(subnode)
        for subnode in node.orelse:
            self.visit(subnode)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Handles ClassDef node and set context."""
        if self.current_classes:
            # ignore class inner class
            return
        self.current_classes.append(node.name)
        self.add_entry(node.name)
        if self.is_final(node.decorator_list):
            self.add_final_entry(node.name)
        self.context.append(node.name)
        self.previous = node
        for child in node.body:
            self.visit(child)
        self.context.pop()
        self.current_classes.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Handles FunctionDef node and set context."""
        # ignore function inner function
        if self.current_function is None:
            self.add_entry(node.name)  # should be called before setting self.current_function
            if self.is_final(node.decorator_list):
                self.add_final_entry(node.name)
            if self.is_overload(node.decorator_list):
                self.add_overload_entry(node)
            self.context.append(node.name)
            self.current_function = node
            for child in node.body:
                self.visit(child)
            self.context.pop()
            self.current_function = None

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Handles AsyncFunctionDef node and set context."""
        self.visit_FunctionDef(node)  # type: ignore
