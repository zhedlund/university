#!/usr/bin/env python3
import random

# Function to generate random English text message from words in a document
def generate_random_english_text(file_path, num_words):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()  # Read words from the file and split by lines
        # Ensure the number of words requested does not exceed the number of words in the document
        num_words = min(num_words, len(words))
        print("Number of words:", num_words)  # Debugging: Print the number of words to be selected
        # Randomly select words from the document
        selected_words = random.sample(words, num_words)
        print("Selected words:", selected_words)  # Debugging: Print the selected words
        # Join the selected words to form the message
        return ' '.join(selected_words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main():
    # File path for English words document
    file_path = "english_words.txt"
    # Number of words for random English text message
    num_words = 10
    
    # Generate random English text message from words in the document
    random_message = generate_random_english_text(file_path, num_words)
    if random_message:
        print("Random English Text Message:")
        print(random_message)

if __name__ == "__main__":
    main()
