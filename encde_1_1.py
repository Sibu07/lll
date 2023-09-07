def encode_to_binary(message):
    binary_code = ""
    for char in message:
        binary_code += bin(ord(char))[2:].zfill(8)  # Convert character to binary code
    return binary_code

def decode_binary(binary_code):
    decoded_message = ""
    for i in range(0, len(binary_code), 8):
        binary_char = binary_code[i:i+8]  # Extract 8-bit binary code for each character
        decoded_message += chr(int(binary_char, 2))  # Convert binary code to character
    return decoded_message

# Example usage
message = input("Enter the message to encode: ")
encoded = encode_to_binary(message)
print("Encoded binary code:", encoded)

decode_code = '''
def decode_binary(binary_code):
    decoded_message = ""
    for i in range(0, len(binary_code), 8):
        binary_char = binary_code[i:i+8]  # Extract 8-bit binary code for each character
        decoded_message += chr(int(binary_char, 2))  # Convert binary code to character
    return decoded_message

binary_code = "{0}"
decoded_message = decode_binary(binary_code)
print("Decoded message:", decoded_message)
'''.format(encoded)

print("Python code for decoding:")
print(decode_code)
