def encrypt(key, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for pad in range(0, len(plaintext) % len(key) * -1 % len(key)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(key)):
        for element in [a - 1 for a in key]:
            ciphertext += plaintext[offset + element]
        ciphertext += " "
    return ciphertext[:-1]

print(encrypt([2,1,3,5,4], "VISHWACTF HELLO WORLD"))
print(encrypt([2,1,3,5,4], "RT1KC _YH43 3DRW_ T1HP_ R3M7U TA1N0"))

"""
VishwaCTF{TR1CKY_H34D3R_W1TH_P3RMU7AT10N}
"""
