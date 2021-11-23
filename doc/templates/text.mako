## Generate Module-Level doc without submodules
## Available context includes `doc_utils`, `module`, `modules` and configs in `config.mako`

<%
from pdoc.doc_utils import get_doc, get_title, render_version
from textwrap import indent
%>

<%def name="h1(s)"># ${s}</%def>
<%def name="h2(s)">## ${s}</%def>
<%def name="h3(s)">### ${s}</%def>
<%def name="h4(s)">#### ${s}</%def>

<%def name="render_params(p_lst, dedent_space=4)">
% for p in p_lst:
${' ' * dedent_space}- `${p.name}`${f' ({p.annotation})' if p.annotation else ''}${render_version(p)}${f': {indent(p.description, " " * 4).lstrip()}' if p.description else ''}

% endfor
</%def>

<%def name="render_function(doc)">
% if doc.description:
- **说明**

${doc.description}

% endif

% if doc.require:
- **要求**${render_version(doc.require)}

% if doc.require.content:
${render_params(doc.require.content)}

% else:
${doc.require}

% endif
% endif
- **参数**${render_version(doc.args)}

% if doc.args.overloads:
    **重载:**

% for i, (title, overload) in enumerate(doc.args.overloads.items()):
    ${i + 1}. `${title}`

${render_params(overload.args, dedent_space=8)}
    返回:

${render_params(overload.returns, dedent_space=8)}
% endfor

% elif doc.args.content:
${render_params(doc.args.content)}
% else:
    无

% endif

% if not doc.args.overloads:
- **返回**${render_version(doc.returns)}

% if doc.returns.content:
${render_params(doc.returns.content)}
% else:
    ${doc.returns}

% endif
% endif

% if doc.raises:
- **异常**${render_version(doc.raises)}

% if doc.raises.content:
${render_params(doc.raises.content)}

% else:
${doc.raises}

% endif
% endif
% if doc.examples:
- **用法**${render_version(doc.examples)}

${doc.examples}
% endif
</%def>

<%def name="render_variable(doc, is_own=True)">
% if is_own:
- **类型:** ${doc.var_type}${render_version(doc.type_version)}

% if doc.description:
% if '\n\n' in doc.description:
- **说明**

${doc.description}

% else:
- **说明:** ${doc.description}

% endif
% endif
% if doc.examples:
- **用法**${render_version(doc.examples)}

${doc.examples}
% endif

% else:
## feature
- **类型:** ${doc.var_type}${render_version(doc.type_version)}

- **说明:** 见父类文档

% endif
</%def>

## Start the output logic for an entire module.
<%
    mod_doc = get_doc(module)
    variables = module.variables()
    classes = module.classes()
    functions = module.functions()
    libraryattrs = module.libraryattrs()
    submodules = module.submodules()
    heading = '命名空间' if module.is_namespace else '模块'
%>
---
contentSidebar: true
sidebarDepth: 0
---

${h1(f"`{module.name}` {heading}")}${render_version(mod_doc.version)}

${mod_doc.description}

% if submodules:
${h2("子模块")}

% for m in submodules:
* [${m.name}](${m.name.split(".")[-1]}/)

% endfor
% endif

% if variables:
% for v in variables:
<% doc = get_doc(v) %>
${h2(get_title(v))}${render_version(doc)}
${render_variable(doc)}
% endfor
% endif
## end of variables render

% if functions:
% for f in functions:
<% doc = get_doc(f) %>
${h2(get_title(f))}${render_version(doc)}
${render_function(doc)}
% endfor
% endif
## end of funtions render

% if classes:
% for c in classes:
<%
    cls_doc = get_doc(c)
    class_vars = c.class_variables()
    inst_vars = c.instance_variables()
    methods = c.methods()
    class_static_methods = c.functions()
    mro = c.mro()
    subclasses = c.subclasses()
%>
${h2(get_title(c))}${render_version(cls_doc)}

% if cls_doc.description:
${cls_doc.description}

% endif

% if mro:
${h3('基类')}

% for cc in mro:
* ${cc.refname}

% endfor
% endif

% if cls_doc.require:
- **要求**${render_version(cls_doc.require)}

% if cls_doc.require.content:
${render_params(cls_doc.require.content)}

% else:
${cls_doc.require}

% endif
% endif

- **参数**${render_version(cls_doc.args)}

% if cls_doc.args.content:
${render_params(cls_doc.args.content)}
% else:
    无

% endif

% if cls_doc.examples:
- **用法**${render_version(cls_doc.examples)}

${cls_doc.examples}
% endif

% if class_vars:
% for v in class_vars:
<% doc = get_doc(v) %>
${h3(get_title(v))}${render_version(doc)}
${render_variable(doc)}
% endfor
% endif

% if inst_vars:
% for v in inst_vars:
<% doc = get_doc(v) %>
${h3(get_title(v))}${render_version(doc)}
${render_variable(doc)}
% endfor
% endif

% if class_static_methods:
% for f in class_static_methods:
<% doc = get_doc(f) %>
${h3(get_title(f))}${render_version(doc)}
${render_function(doc)}
% endfor
% endif

% if methods:
% for m in methods:
<% doc = get_doc(m) %>
${h3(get_title(m))}${render_version(doc)}
${render_function(doc)}
% endfor
% endif

% endfor
% endif
## end of classes render

% for l in libraryattrs:
## <% doc = get_doc(l) %>
${h3(get_title(l))}

${l.docstring}

% endfor
