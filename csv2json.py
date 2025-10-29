import csv, json, sys

def csv_to_json(csv_text):
    reader = csv.DictReader(csv_text.splitlines())
    return json.dumps(list(reader), ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv2json.py path/to/file.csv", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        print(csv_to_json(f.read()))
