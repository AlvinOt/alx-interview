# UTF-8 decoding function
def decode_utf8(data):
    result = ""
    i = 0

    while i < len(data):
        byte = data[i]

        # Determine the number of bytes for the character
        if byte & 0b10000000 == 0:
            # Single-byte character
            result += chr(byte)
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            # Two-byte character
            result += chr(((byte & 0b00011111) << 6) | (data[i + 1] & 0b00111111))
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            # Three-byte character
            result += chr(((byte & 0b00001111) << 12) | ((data[i + 1] & 0b00111111) << 6) | (data[i + 2] & 0b00111111))
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            # Four-byte character
            result += chr(((byte & 0b00000111) << 18) | ((data[i + 1] & 0b00111111) << 12) | ((data[i + 2] & 0b00111111) << 6) | (data[i + 3] & 0b00111111))
            i += 4

    return result

# Test case
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
decoded_string = decode_utf8(data)
print(decoded_string)

