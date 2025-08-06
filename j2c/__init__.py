import argparse
from pathlib import Path
import sys
from .j2c import json_to_csv


def main():
    parser = argparse.ArgumentParser(
        description='JSON logs to CSV table converter.')
    parser.add_argument(
        '-i',
        '--in',
        help='Input path to JSON log file.',
        required=True)
    parser.add_argument(
        '-o',
        '--out',
        help='Output path to save CSV.',
        required=True)
    parser.add_argument('-d', '--delimiter', default=',',
                        help='Delimiter (default is ",")')

    args = parser.parse_args()

    input_path = Path(getattr(args, 'in'))
    output_path = Path(getattr(args, 'out'))
    delimiter = getattr(args, 'delimiter')

    sys.exit(json_to_csv(input_path, output_path, delimiter))


if __name__ == "__main__":
    main()
