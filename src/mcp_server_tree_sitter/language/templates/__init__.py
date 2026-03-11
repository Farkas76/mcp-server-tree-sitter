"""Language-specific query templates collection.

Each language module exports a TEMPLATES dict mapping template names to
tree-sitter query strings. Every language MUST provide at least the
REQUIRED_KEYS templates.

Capture group naming conventions:
  - @<type>.name   — the identifier/name of the symbol
  - @<type>.body   — the body block (optional field where applicable)
  - @<type>.params — parameter list (functions)
  - @<type>.def    — the entire declaration node
  - @import.*      — import-related captures (language-specific sub-names)

Where <type> matches the template key in singular form:
  functions  -> @function.*
  classes    -> @class.*
  structs    -> @struct.*
  imports    -> @import.*
  interfaces -> @interface.*
"""

from . import (
    apl,
    c,
    cpp,
    go,
    java,
    javascript,
    julia,
    kotlin,
    python,
    rust,
    swift,
    typescript,
)

# Every language must provide at least these template keys
REQUIRED_KEYS = frozenset({"functions", "imports"})

# Combine all language templates
QUERY_TEMPLATES: dict[str, dict[str, str]] = {
    "python": python.TEMPLATES,
    "javascript": javascript.TEMPLATES,
    "typescript": typescript.TEMPLATES,
    "go": go.TEMPLATES,
    "rust": rust.TEMPLATES,
    "c": c.TEMPLATES,
    "cpp": cpp.TEMPLATES,
    "swift": swift.TEMPLATES,
    "java": java.TEMPLATES,
    "kotlin": kotlin.TEMPLATES,
    "julia": julia.TEMPLATES,
    "apl": apl.TEMPLATES,
}


def validate_templates() -> list[str]:
    """Validate that all languages provide the required template keys.

    Returns list of error messages (empty if all valid).
    """
    errors = []
    for language, templates in QUERY_TEMPLATES.items():
        missing = REQUIRED_KEYS - templates.keys()
        if missing:
            errors.append(f"{language}: missing required templates {missing}")
    return errors
