# Program to perform AND and XOR with 127 on each character of a string
# 🔹 Take input from user
s = input("Enter a string: ")

print("\nOriginal String:")
print(s)

# 🔹 AND operation with 127
and_result = ''.join(chr(ord(c) & 127) for c in s)

# 🔹 XOR operation with 127
xor_result = ''.join(chr(ord(c) ^ 127) for c in s)

print("\nAND with 127 Result:")
print(and_result)

print("\nXOR with 127 Result:")
print(xor_result)

# 🔹 Optional (recommended for exam clarity)
print("\nASCII values after XOR with 127:")
for c in s:
    print(f"{repr(c)} -> {ord(c)} ^ 127 = {ord(c) ^ 127}")