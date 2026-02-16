import argparse
import csv
import os
from pathlib import Path

from tabulate import tabulate

from reports.loader import REPORTS

BASE_DIR = Path("csv_files")


def read_rows(files: list[str], base_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for filename in files:
        with open(base_dir / filename, encoding="utf-8") as f:
            rows.extend(list(csv.DictReader(f)))
    return rows


def get_available_files(path: Path) -> set[str]:
    return set(os.listdir(path))


def main(argv=None, base_dir=BASE_DIR):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="specify the names of the files in the 'csv_files' directory "
             "for generating the report",
    )
    parser.add_argument(
        "--report",
        choices=REPORTS.keys(),
        required=True,
        help="specify one of the available report names to generate",
    )
    args = parser.parse_args(argv)

    csv_files = get_available_files(base_dir)
    if not set(args.files).issubset(csv_files):
        parser.error("unknown file name")

    rows =read_rows(args.files, base_dir)
    data = REPORTS[args.report](rows)
    print(tabulate(data, headers="keys", tablefmt="psql", floatfmt=".2f"))


if __name__ == "__main__":
    main()
