import json
import sys
import csv
from pathlib import Path


def json_to_csv(input_file: Path, output_file: Path, delimiter_sym: str):
    # We collect all keys from all objects for CSV headers.
    fieldnames = dict()

    # First pass: collect all possible fields.
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line.strip())
                for key in data.keys():
                    if key not in fieldnames:
                        fieldnames[key] = None
            except json.JSONDecodeError as e:
                print(
                    f"Failed to read the line {line_num}: {line.strip()}. Error: {e}",
                    file=sys.stderr)
                return 1

    if not fieldnames:
        print("No valid JSON object detected in source", file=sys.stderr)
        return 1

    # Second pass: write data.
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames.keys(),
            delimiter=delimiter_sym)
        writer.writeheader()

        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    data = json.loads(line.strip())
                    writer.writerow(data)
                except json.JSONDecodeError as e:
                    print(
                        f"Skip line {line_num}: {line.strip()}. Error: {e}",
                        file=sys.stderr)
                    return 1

    return 0
