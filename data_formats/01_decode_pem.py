from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

with open('example.pem', 'rb') as pem_file:
    data = pem_file.read()

key = load_pem_private_key(data, password=None)
if isinstance(key, rsa.RSAPrivateKey):
    private_numbers = key.private_numbers()
    print(f"d = {private_numbers.d}")