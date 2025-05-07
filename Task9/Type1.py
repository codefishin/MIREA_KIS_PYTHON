import re


def main(input_string):
    pattern = r'global\s+(\w+)\s+is\s*#(-?\d+)'
    matches = re.findall(pattern, input_string)
    result = {}
    for key, value in matches:
        result[key] = int(value)

    return result
  
