# JSON to CSV Converter (j2c)
A lightweight Python tool that converts newline-delimited JSON files to CSV with automatic header detection. Handles nested keys, custom delimiters, and malformed JSON with error reporting.

## Features
- Converts JSON log files (one JSON object per line without commas at the end) to CSV format;
- Automatically detects all JSON fields and creates appropriate CSV headers;
- Handles malformed JSON lines with error reporting;
- Configurable output delimiter;
- Easy command-line interface.

## Installation
```bash
pip install git+https://github.com/Alp4ka/j2c.git
```

## Usage
### CLI
```bash
j2c -i input.json -o output.csv [-d DELIMITER]
```
Arguments:

- `-i/--in`: Input JSON file path (required);
- `-o/--out`: Output CSV file path (required);
- `-d/--delimiter`: Delimiter character (default: ',').


## Example
Input JSON (`logs.json`):

```json
{"name": "Alice", "age": 25, "city": "New York"}
{"name": "Bob", "age": 30, "country": "Canada"}
```

Command:
```bash
j2c -i input.json -o output.csv
```

Output CSV (`output.csv`):
```text
name,age,city,country
Alice,25,New York,
Bob,30,,Canada
```

## Error Handling
The script will:
- Skip malformed JSON lines and report errors to stderr;
- Exit with non-zero status if no valid JSON objects are found;
- Report lines where errors occur.

## Dependencies
- Python 3.6+
- Standard Python libraries only (no external dependencies)

## License
[MIT License](./LICENSE)