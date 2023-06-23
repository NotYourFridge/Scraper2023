def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


with open('all_colors.txt', 'r') as f:
    hex_codes = [line.strip() for line in f.readlines()]


with open('rgb_values.txt', 'w') as f:
    for hex_code in hex_codes:
        rgb = hex_to_rgb(hex_code)
        f.write(f'{rgb}\n')