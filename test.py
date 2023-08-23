from libs.encryption.symmetric.symmetric import TELSymmetric

TELS = TELSymmetric(iterations=100000, salt_length=128, key_length=128)

plaintext = "Hello World"
ciphertext = TELS.encrypt(plaintext=plaintext, password="password")
decrpytedplaintext = TELS.decrypt(ciphertext=ciphertext, password="password")

print(plaintext)
print(ciphertext)
print(decrpytedplaintext)