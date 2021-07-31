cipher_text= "MKTKXGR XOJK IAXOUAY XOJK"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
for offset in range(1,25):
    new_sentence = ""
    for char in cipher_text.upper():
        position = alphabet.find(char)
        if position > -1:
            new_char = alphabet[position+offset]
        else:
            # usually a space or comma
            new_char = char
        new_sentence = new_sentence + new_char
    print(new_sentence)
