#!/usr/bin/env python3
import random

# Function to generate a random 16-bit key
def generate_random_key():
    return random.randint(0, 2**16 - 1)

# Function to pad a message with a blank character if its length is odd
def pad_message(message):
    if len(message) % 2 != 0:
        message += " "
    return message

# Function to encrypt a message using the toy symmetric cryptosystem
def encrypt(message, key):
    repeated_key = (key.to_bytes(2, 'big') * (len(message) // 2))
    ciphertext = ""
    for char, key_char in zip(message, repeated_key):
        encrypted_char = chr(ord(char) ^ key_char)
        ciphertext += encrypted_char
    return ciphertext

# Function to decrypt a ciphertext using the toy symmetric cryptosystem
def decrypt(ciphertext, key):
    repeated_key = (key.to_bytes(2, 'big') * (len(ciphertext) // 2))
    decrypted = ""
    for char, key_char in zip(ciphertext, repeated_key):
        decrypted_char = chr(ord(char) ^ key_char)
        decrypted += decrypted_char
    return decrypted

# Test the cryptosystem
def main():
    message = "Hello, this is a secret message."
    message = pad_message(message)
    key = generate_random_key()
    ciphertext = encrypt(message, key)
    print("Original Message:", message)
    print("Encrypted Message:", ciphertext)

    decrypted = decrypt(ciphertext, key)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
