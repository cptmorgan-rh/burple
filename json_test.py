import json


def extract_json_objects(text, decoder=json.JSONDecoder()):
    """Find JSON objects in text, and yield the decoded JSON data

    Does not attempt to look for JSON arrays, text, or other JSON types outside
    of a parent JSON object.

    """
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


example = open("./json.txt", "r")

json_output = []

for result in extract_json_objects(example.read()):
    if 'error' in result["message"]:
        json_output.append(result)

json_dates = {}

for item in json_output:
    if item["date"] in json_dates:
        json_dates[item["date"]] += 1
    else:
        json_dates[item["date"]] = 1

for k, v in json_dates.items():
    print(f"{k} - {v}")
