from cryptography import x509

with open('example.der','rb') as file_data:
    der_data = file_data.read()

cert = x509.load_der_x509_certificate(der_data)
public_key = cert.public_key()
public_numbers = public_key.public_numbers()
print(f"Modulus of cert: {public_numbers.n}")