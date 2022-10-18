import argparse
from typing import Sequence
import json


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename, mode="r", encoding="utf8") as f:
                data = json.load(f)
                cells = data["cells"]
                outputs_lengths = (len(cell["outputs"]) for cell in cells)

                if any(l > 0 for l in outputs_lengths):
                    retval = 1

        except json.JSONDecodeError as exc:
            print(f"{filename}: {exc}")
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
