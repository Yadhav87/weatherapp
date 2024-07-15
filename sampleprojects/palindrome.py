def is_palindrome(text):
    clean_text ="".join(char.lower() for char in text if char.isalnum)
    return clean_text == clean_text[:: -1]
text ="Race car"
if  is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome")