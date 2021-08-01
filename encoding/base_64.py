import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_string = bytes.fromhex(hex_string)

base64_string = base64.b64encode(bytes_string)
print(base64_string)

# # encoding
# test = "test123 test456"
# encoded = base64.b64encode(test.encode()).decode()
# print(encoded)
# decoded = base64.b64decode(encoded).decode()
# print(decoded)
