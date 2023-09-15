#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Load an object from a JSON file and return it."""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
