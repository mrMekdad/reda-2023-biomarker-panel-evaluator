"""Core workflow for Biomarker Panel Evaluator by Red@."""

PROJECT_NAME = "Biomarker Panel Evaluator"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
