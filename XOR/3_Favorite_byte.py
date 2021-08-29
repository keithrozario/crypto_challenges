"""
single_byte_xor courtesy of
https://www.codementor.io/@arpitbhayani/deciphering-single-byte-xor-ciphertext-17mtwlzh30
"""


def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])


data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
print(bytes.fromhex(data))

for x in range(256):
    decrypted_text = single_byte_xor(
                        text=bytes.fromhex(data),
                        key=x
                    )
    try:
        if decrypted_text.decode('utf-8')[:6] == "crypto":
            print(f"key:{x}, decrypted: {decrypted_text}")
    except UnicodeDecodeError:
        pass



