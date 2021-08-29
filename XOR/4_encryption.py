from pwn import xor
encrypted_text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
text = b"crypto{"
encrypted_text_bytes = bytes.fromhex(encrypted_text)

print(xor(text, encrypted_text_bytes))
# b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'

key = b'myXORkey'
print(xor(key, encrypted_text_bytes))