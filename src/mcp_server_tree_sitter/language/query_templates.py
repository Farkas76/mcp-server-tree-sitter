"""Query templates for common code patterns by language."""

from typing import Any

from .templates import QUERY_TEMPLATES


def get_query_template(language: str, template_name: str) -> str | None:
    """
    Get a query template for a language.

    Args:
        language: Language identifier
        template_name: Template name

    Returns:
        Query string or None if not found
    """
    language_templates = QUERY_TEMPLATES.get(language)
    if language_templates:
        return language_templates.get(template_name)
    return None


def list_query_templates(language: str | None = None) -> dict[str, Any]:
    """
    List available query templates.

    Args:
        language: Optional language to filter by

    Returns:
        Dictionary of templates by language
    """
    if language:
        return {language: QUERY_TEMPLATES.get(language, {})}
    return QUERY_TEMPLATES
