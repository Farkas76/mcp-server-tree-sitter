"""Tests that validate all language query templates parse correctly."""

import pytest
from tree_sitter import Query
from tree_sitter_language_pack import get_language

from mcp_server_tree_sitter.language.templates import (
    QUERY_TEMPLATES,
    REQUIRED_KEYS,
    validate_templates,
)


def test_all_languages_have_required_keys():
    """Every language must provide at least 'functions' and 'imports' templates."""
    errors = validate_templates()
    assert not errors, "Template validation errors:\n" + "\n".join(errors)


# Map template language names to tree-sitter-language-pack names
LANGUAGE_PACK_NAMES = {
    "python": "python",
    "javascript": "javascript",
    "typescript": "typescript",
    "go": "go",
    "rust": "rust",
    "c": "c",
    "cpp": "cpp",
    "swift": "swift",
    "java": "java",
    "kotlin": "kotlin",
    "julia": "julia",
    "apl": "apl",
}


def _get_all_template_params():
    """Generate (language, template_name, query_string) params for parametrized tests."""
    params = []
    for language, templates in QUERY_TEMPLATES.items():
        for template_name, query_string in templates.items():
            params.append(
                pytest.param(language, template_name, query_string, id=f"{language}/{template_name}")
            )
    return params


@pytest.mark.parametrize("language,template_name,query_string", _get_all_template_params())
def test_template_parses_without_error(language, template_name, query_string):
    """Each query template must parse against its language grammar without errors."""
    pack_name = LANGUAGE_PACK_NAMES.get(language)
    if pack_name is None:
        pytest.skip(f"No language pack mapping for {language}")

    try:
        lang = get_language(pack_name)
    except Exception:
        pytest.skip(f"Language {pack_name} not available in language pack")

    # This will raise if the query has syntax errors or references invalid node types
    Query(lang, query_string)


def test_required_keys_are_minimal():
    """Sanity check: REQUIRED_KEYS should contain functions and imports."""
    assert "functions" in REQUIRED_KEYS
    assert "imports" in REQUIRED_KEYS
