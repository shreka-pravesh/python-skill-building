# Check if a word or sentence is a palindrome

def is_palindrome(text):
    # Remove spaces and convert to lowercase for accurate comparison
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]
user_input = input("Enter a word or sentence: ")
if is_palindrome(user_input):
    print("Yes, it's a Palindrome")
else:
    print("No, it's not a Palindrome")
