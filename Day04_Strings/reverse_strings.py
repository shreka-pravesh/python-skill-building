# Reverse a string using slicing

def reverse_text(text):
    # This line reverses the string using Python slicing
    return text[::-1]
user_text = input("Enter any word or sentence: ")
print("Reversed text:", reverse_text(user_text))
