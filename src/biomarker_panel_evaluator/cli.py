import argparse
from biomarker_panel_evaluator.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluation utilities for biomarker candidate panels and score summaries.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
