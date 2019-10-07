def parse_properties(file):
    line = file.read()
    key, value = line.split('=')
    return {key: value}