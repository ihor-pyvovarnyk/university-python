def parse_properties(file):
    properties = {}
    for line in file:
        key, value = line.split('=')
        properties[key] = value.rstrip()
    return properties