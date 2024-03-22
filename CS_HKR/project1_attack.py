#!/usr/bin/env python3
import random
import string

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

# Function to generate random English text messages
def generate_random_english_message(word_list, num_words):
    selected_words = random.sample(word_list, num_words)
    return ' '.join(selected_words)

# Brute-force decryption attack
def brute_force_decrypt(ciphertext):
    for key in range(2**16):
        decrypted = decrypt(ciphertext, key)
        if is_english(decrypted):
            return decrypted, key  # Return the decrypted message and the key
    return None, None  # Return None if decryption fails

# Function to determine if text is English
def is_english(text):
    # Define a set of English characters
    english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!?")
    
    # Check if all characters in the text are English characters
    for char in text:
        if char not in english_chars:
            return False
    return True

# Test the cryptosystem
def main():
    with open("english_words.txt", "r") as f:
        word_list = [word.strip() for word in f]

    message = generate_random_english_message(word_list, 5)  # Generate a random English text message
    message = pad_message(message)
    key = generate_random_key()
    ciphertext = encrypt(message, key)
    print("Original Message:", message)
    print("Encrypted Message:", ciphertext)

    # Decrypt using the original decryption method
    decrypted = decrypt(ciphertext, key)
    print("Decrypted Message (Original):", decrypted)

    # Attempt brute-force decryption attack
    brute_decrypted, brute_key = brute_force_decrypt(ciphertext)
    print("Decrypted Message (Brute-force):", brute_decrypted)
    print("Brute-force Decryption Key:", brute_key)
    if decrypted == brute_decrypted:
	    print("Brute-force Decryption successful")
    else:
	    print("Brute-force Decryption failed")

if __name__ == "__main__":
    main()
