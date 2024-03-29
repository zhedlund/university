from langdetect import detect

def is_this_english(text):
    try:
        # Attempt to detect the language of the text
        language = detect(text)
        # Check if the detected language is English
        return language == 'en'
    except:
        # Handle the case where language detection fails
        return False

# Test the is_english function
text = "wrack loan stole grisly circularizes"
print("Is English:", is_this_english(text))  # Output: True
