"""Query templates for Julia language."""

TEMPLATES = {
    "functions": """
        (function_definition
            (signature
                (call_expression
                    (identifier) @function.name
                    (argument_list) @function.params))) @function.def

        (assignment
            (call_expression
                (identifier) @function.name
                (argument_list) @function.params)) @function.short_def
    """,
    "modules": """
        (module_definition
            name: (identifier) @module.name) @module.def
    """,
    "structs": """
        (struct_definition
            (type_head
                (identifier) @struct.name)) @struct.def
    """,
    "imports": """
        (import_statement) @import

        (import_statement
            (identifier) @import.name) @import.simple

        (using_statement) @using

        (using_statement
            (identifier) @using.name) @using.simple

        (import_statement
            (import_path) @import.qualified) @import.qualified
    """,
    "macros": """
        (macro_definition
            (signature
                (call_expression
                    (identifier) @macro.name))) @macro.def
    """,
    "abstractTypes": """
        (abstract_definition
            (type_head
                (identifier) @abstract.name)) @abstract.def
    """,
}
