k = 23
plaintext = "LeThiTienDung"
ciphertext = ""

for ch in plaintext:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        ciphertext += chr((ord(ch) - base + k) % 26 + base)
    else:
        ciphertext += ch
print("Ciphertext:", ciphertext)
