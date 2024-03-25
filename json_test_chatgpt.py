import json
from collections import Counter


def extract_json_objects(text):
    """Find JSON objects in text, and yield the decoded JSON data"""
    decoder = json.JSONDecoder()
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1


json_dates = Counter()

with open("./json.txt", "r") as file:
    for line in file:
        for result in extract_json_objects(line):
            if 'error' in result.get("message", {}):
                json_dates[result.get("date", "Unknown")] += 1


for k, v in json_dates.items():
    print(f"{k} - {v}")
