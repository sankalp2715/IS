# DES Encryption and Decryption in Python

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# 🔹 Key must be exactly 8 bytes
key = b'8bytekey'

# 🔹 Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

# 🔹 Take input from user
text = input("Enter message: ").encode()

# 🔹 Encryption
encrypted = cipher.encrypt(pad(text, 8))
print("\nEncrypted (bytes):", encrypted)

# 🔹 Decryption
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted (original):", decrypted.decode())