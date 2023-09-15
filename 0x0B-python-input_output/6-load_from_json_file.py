#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Load an object from a JSON file and return it."""
    try:
        with open(filename, 'r') as file:
            obj = json.load(file)
        return obj
    except json.JSONDecodeError as e:
        raise ValueError(f'{e.msg}: line {e.lineno} column {e.colno} (char {e.pos})')
