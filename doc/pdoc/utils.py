import re
import enum
import inspect
from typing import List, Optional
from inspect import Signature, Parameter

from pdoc.pycode.annotransformer import formatannotation, convert_anno_new_style


def signature_repr(sig: Signature, returns: Optional[List[str]] = None) -> str:
    """
    Represent inspect.Signature without annotation.

    This function solve Parameter default value represent.
    But do not show return annotation. (which cause a redudant output)

    Args:
        sig: a signature object
        returns: if given, then represent params with returns
    """

    def safe_default_value(p: Parameter) -> Parameter:
        value = p.default
        if value is Parameter.empty:
            return p

        replacement = None
        if not replacement:
            if isinstance(value, enum.Enum):
                replacement = str(value)
            elif value is Ellipsis:
                replacement = '...'
            elif inspect.isclass(value):
                replacement = value.__name__
            elif ' at 0x' in repr(value):
                replacement = re.sub(r' at 0x\w+', '', repr(value))

        if replacement:
            class mock:
                def __repr__(self):
                    return replacement
            return p.replace(default=mock())
        return p

    # Duplicated from `inspect.Signature.__str__`, remove all annotation
    result = []
    render_pos_only_separator = False
    render_kw_only_separator = True
    for param in sig.parameters.values():
        param = safe_default_value(param)
        param = param.replace(annotation=Parameter.empty)
        formatted = str(param)

        kind = param.kind

        if kind == Parameter.POSITIONAL_ONLY:
            render_pos_only_separator = True
        elif render_pos_only_separator:
            result.append('/')
            render_pos_only_separator = False

        if kind == Parameter.VAR_POSITIONAL:
            render_kw_only_separator = False
        elif kind == Parameter.KEYWORD_ONLY and render_kw_only_separator:
            result.append('*')
            render_kw_only_separator = False

        result.append(formatted)

    if render_pos_only_separator:
        result.append('/')

    rendered = '({})'.format(', '.join(result))

    if returns:
        rendered += ' -> {}'.format(' | '.join(returns))

    return rendered
