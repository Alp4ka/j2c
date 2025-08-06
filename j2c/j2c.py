import json
import sys
import csv
from pathlib import Path
from collections import abc, OrderedDict
from typing import Dict

_SEP = '.'


def _flatten_dict(d: Dict, parent_key: str = '',
                  sep: str = _SEP) -> OrderedDict:
    """Flatten dictionary while maintaining key order using OrderedDict."""
    items = OrderedDict()
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, abc.MutableMapping):
            items.update(_flatten_dict(v, new_key, sep))
        else:
            items[new_key] = str(v) if v is not None else ''
    return items


def json_to_csv(input_file: Path, output_file: Path,
                delimiter_sym: str) -> int:
    """
    Convert JSON logs to CSV while maintaining field order from first occurrence.
    Uses single-pass processing when possible.
    """
    field_order = OrderedDict()  # Maintains insertion order for fields.
    rows = []
    has_errors = False

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:  # Skip empty lines.
                continue

            try:
                # Get flattened data with original field order.
                data = _flatten_dict(json.loads(line))

                # Update field order with new keys (maintains first occurrence order).
                for key in data.keys():
                    if key not in field_order:
                        field_order[key] = None

                rows.append(data)
            except json.JSONDecodeError as e:
                print(
                    f"Skip line {line_num}: {line}. Error: {e}",
                    file=sys.stderr)
                has_errors = True
                continue

    if not field_order:
        print("No valid JSON object detected in source", file=sys.stderr)
        return 1

    # Write data with fields in order of first appearance.
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=field_order.keys(),
            delimiter=delimiter_sym,
            extrasaction='ignore'  # Ignore extra keys not in fieldnames.
        )
        writer.writeheader()
        writer.writerows(rows)

    return 1 if has_errors else 0
