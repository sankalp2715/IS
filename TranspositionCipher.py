# Transposition Cipher: Encryption and Decryption

def encrypt(message, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key

    return ''.join(cipher)


def decrypt(cipher, key):
    num_cols = key
    num_rows = len(cipher) // key + (len(cipher) % key != 0)
    num_shaded = (num_cols * num_rows) - len(cipher)

    plain = [''] * num_rows

    col = 0
    row = 0

    for symbol in cipher:
        plain[row] += symbol
        row += 1

        if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded):
            row = 0
            col += 1

    return ''.join(plain)


# 🔹 Driver Code (important for practical)
message = input("Enter message: ")
key = int(input("Enter key: "))

cipher_text = encrypt(message, key)
print("\nEncrypted Text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)