#!/usr/bin/env python3

import random

def generate_random_key():
    return random.randint(0, 2**16 - 1)

def encrypt(message, key):
    ciphertext = ""
    for char in message:
        encrypted_char = chr(ord(char) ^ key)
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        decrypted += decrypted_char
    return decrypted

def main():
    message = "Hello, this is a secret message."
    key = generate_random_key()
    ciphertext = encrypt(message, key)
    print("Original Message:", message)
    print("Encrypted Message:", ciphertext)

    decrypted = decrypt(ciphertext, key)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()

