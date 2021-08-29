from cryptography.hazmat.primitives import serialization

with open('example.pub', 'rb') as file:
    public_key_ssh = file.read()

rsa_public_key = serialization.load_ssh_public_key(public_key_ssh)
rsa_public_numbers = rsa_public_key.public_numbers()
rsa_modulus = rsa_public_numbers.n

print(f"Modulus of Public Key: {rsa_modulus}")