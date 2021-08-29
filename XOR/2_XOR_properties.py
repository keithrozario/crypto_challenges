from pwn import xor

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
print(f"Key2: {bytes.fromhex(KEY1)}")

KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"

# Associative and Identity
# 1 ^ 2 ^ 1 = 1 ^ 1 ^ 2 = 0 ^ 2 = 2
KEY2_in_bytes = xor(bytes.fromhex(KEY1), bytes.fromhex(KEY2_XOR_KEY1))
print(f"Key2: {KEY2_in_bytes}")

KEY2_XOR_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

# Associative and Identity
# 2 ^ 3 ^ 2 = 2 ^ 2 ^ 3 = 0 ^ 3 = 3
KEY3_in_bytes = xor(KEY2_in_bytes, bytes.fromhex(KEY2_XOR_KEY3))
print(f"Key3: {KEY3_in_bytes}")

FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Multiply by KEY1, Key2, and Key3 gives us the flag
FLAG = xor(
    bytes.fromhex(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2),
    KEY3_in_bytes,
    KEY2_in_bytes,
    bytes.fromhex(KEY1)
)
print(FLAG)