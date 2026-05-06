from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 🔹 16-byte key (AES-128)
key = b'0123456789abcdef'

cipher = AES.new(key, AES.MODE_ECB)

# 🔹 Take input
text = input("Enter message: ").encode()

# 🔹 Encryption
encrypted = cipher.encrypt(pad(text, 16))
print("\nEncrypted:", encrypted)

# 🔹 Decryption
decrypted = unpad(cipher.decrypt(encrypted), 16)
print("Decrypted:", decrypted.decode())