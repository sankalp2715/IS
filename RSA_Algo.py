#sudo apt update
#sudo apt install python3-pip
#python3 -m pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 🔹 Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()

# 🔹 Create cipher with public key
cipher_encrypt = PKCS1_OAEP.new(public_key)

# 🔹 Input message
message = input("Enter message: ").encode()

# 🔹 Encrypt
encrypted = cipher_encrypt.encrypt(message)
print("\nEncrypted:", encrypted)

# 🔹 Decrypt using private key
cipher_decrypt = PKCS1_OAEP.new(key)
decrypted = cipher_decrypt.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
