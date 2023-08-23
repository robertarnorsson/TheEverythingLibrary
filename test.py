# Symmetrical encryption and decryption example

from libs.encryption.symmetric.symmetric import TELSymmetric

TELS = TELSymmetric(iterations=100000, salt_length=128, key_length=128)

plaintext = "Hello World"
print(plaintext)

ciphertext = TELS.encrypt(plaintext=plaintext, password="password")
print(ciphertext)

decrpytedplaintext = TELS.decrypt(ciphertext=ciphertext, password="password")
print(decrpytedplaintext)

print('--------------------------------------------------------------------------')

# Asymmetrical encryption and decryption example

from libs.encryption.asymmetric.asymmetric import TELAsymmetric

TELA = TELAsymmetric()

private_key, public_key = TELA.generate_key_pair()

TELA.store_private_key(private_key=private_key, password="password", path='', file_name='private_key')
TELA.store_public_key(public_key=public_key, path='', file_name='public_key')

private_key = TELA.get_private_key(password="password", path='', file_name='private_key')
public_key = TELA.get_public_key(path='', file_name='public_key')

plaintext = "Hello World"
print(plaintext)

ciphertext = TELA.encrypt(plaintext=plaintext, public_key=public_key)
print(ciphertext)

decrpytedplaintext = TELA.decrypt(ciphertext=ciphertext, private_key=private_key)
print(decrpytedplaintext)
