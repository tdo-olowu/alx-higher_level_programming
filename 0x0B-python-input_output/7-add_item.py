#!/usr/bin/python3
"""a cmdline program which appends its args to a list then
saves that into a json file"""


if __name__ == "__main__":
    import sys
    import json

    av = sys.argv[1:]

    filename = "add_item.json"
    load_from_j = __import__('6-load_from_json_file').load_from_json_file
    save_to_j = __import__('5-save_to_json_file').save_to_json_file

    existing_args = load_from_j(filename)
    new_args = existing_args + av
    save_to_j(new_args, filename)
