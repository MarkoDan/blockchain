from backend.util.crypto_hash import crypto_hash

HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}


def hex_to_binary(string):
    binary_string = ""
    for char in string:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[char]
    
    return binary_string

# def main():
#     number = 451
#     hex_number = hex(number)

#     binary_number = hex_to_binary(hex_number)
#     print(binary_number)
#     original_number = int(binary_number, 2)
#     print(original_number)

#     hex_to_binary_crypto_hash = hex_to_binary(crypto_hash('test-data'))
#     print(hex_to_binary_crypto_hash)

# main()