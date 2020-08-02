import argparse
import json
import os
import sys

import anonymizer


def find_json_file() -> str:
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        ext = filename.split('.')[-1]
        if ext.lower() == 'json':
            return os.path.realpath(filename)


def read_file(file_path) -> str:
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content


parser = argparse.ArgumentParser(description='CLI to anonymize JSON file')
parser.add_argument('--version', action='version', version='v0.1.0')
parser.add_argument('--empty-string', type=bool, const=True, default=False, nargs='?', help='Empty all string')
parser.add_argument('json_file_path', metavar='json_file', type=str, nargs='?', help='JSON file path')

args = parser.parse_args()

if args.json_file_path:
    try:
        json_content = json.loads(read_file(args.json_file_path))
    except FileNotFoundError:
        print(f'JSON file not found: \'{args.json_file_path}\'')
        sys.exit(1)
else:
    json_file_path = find_json_file()
    if json_file_path is None:
        print('No json file found')
        sys.exit(1)
    json_content = json.loads(read_file(json_file_path))

anonymized_data = anonymizer.anonymize(json_content, empty_string=args.empty_string)
print(json.dumps(anonymized_data))
