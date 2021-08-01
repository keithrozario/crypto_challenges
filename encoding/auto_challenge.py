from pwn import *
import json
import codecs


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(encoding, encoded_message):
    if encoding == "base64":
        decoded = base64.b64decode(encoded_message).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded_message).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded_message, 'rot_13')
    elif encoding == "bigint":
        decoded = bytes.fromhex(encoded_message[2:]).decode()
    elif encoding == "utf-8":
        decoded = "".join(chr(x) for x in encoded_message)
    else:
        print("No matching encoding found!")
        exit(1)

    return decoded


r = remote('socket.cryptohack.org', 13377, level='debug')

end = True

while end:
    received = json_recv()

    if "flag" in received.keys():
        print(f"Flag {received['flag']}")
        end = False
    else:
        print(f"Received type: {received['type']}")
        print(f"Received encoded value: {received['encoded']}")
        decoded_msg = decode(received['type'], received['encoded'])
        print(f"Decoded Message: {decoded_msg}")

        to_send = {
            "decoded": decoded_msg
        }
        json_send(to_send)