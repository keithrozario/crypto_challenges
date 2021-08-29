word = "label"
new_word = ""
for char in word:
    integer = ord(char)
    xor_result = integer ^ 13
    new_char = chr(xor_result)
    new_word += new_char

print(new_word)


