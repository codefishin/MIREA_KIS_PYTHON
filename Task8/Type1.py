def main(_hex):
    value = int(_hex, 16)
    masks = {
        'M1': (0b1, 0),
        'M2': (0b111111111, 1),
        'M4': (0b111, 19)
    }

    result = []
    for field, (mask, shift) in masks.items():
        field_value = (value >> shift) & mask
        result.append((field, field_value))

    return result
  
