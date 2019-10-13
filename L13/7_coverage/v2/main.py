def parse_properties(file):
    properties = {}
    for line in file:
        if line.startswith('#'):
            continue
        key, value = line.split('=')
        properties[key] = value.rstrip()
    return properties