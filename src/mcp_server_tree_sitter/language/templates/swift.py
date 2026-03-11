"""Query templates for Swift language."""

TEMPLATES = {
    "functions": """
        (function_declaration
            name: (simple_identifier) @function.name
            body: (function_body)? @function.body) @function.def
    """,
    "classes": """
        (class_declaration
            name: (type_identifier) @class.name
            body: (class_body)? @class.body) @class.def
    """,
    "structs": """
        (class_declaration
            name: (type_identifier) @struct.name
            body: (class_body)? @struct.body) @struct.def
    """,
    "imports": """
        (import_declaration) @import
    """,
    "protocols": """
        (protocol_declaration
            name: (type_identifier) @protocol.name
            body: (protocol_body)? @protocol.body) @protocol.def
    """,
    "extensions": """
        (class_declaration
            name: (user_type) @extension.name
            body: (class_body)? @extension.body) @extension.def
    """,
}
