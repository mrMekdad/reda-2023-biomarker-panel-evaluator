"""Core workflow for Biomarker Panel Evaluator by Red@."""

PROJECT_NAME = "Biomarker Panel Evaluator"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": "bioinformatics"}
