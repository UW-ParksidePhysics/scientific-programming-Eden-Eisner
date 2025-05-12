def parse_constants_file(filename="constants.txt"):
    constants = {}
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.strip() and not line.lower().startswith("name") and "-" not in line:
            name = line[:26].strip().lower()
            value_str = line[26:46].strip()
            dimension = line[46:].strip()

            try:
                value = float(value_str)
                constants[name] = {
                    'value': value,
                    'dimension': dimension
                }
            except ValueError:
                continue  # Skip lines with non-numeric values

    return constants


# Example usage:
if __name__ == "__main__":
    constants = parse_constants_file("constants.txt")
    for name, info in constants.items():
        print(f"{name.title():25} = {info['value']} [{info['dimension']}]")
