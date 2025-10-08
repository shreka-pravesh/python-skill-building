# Count the total number of words and characters in a sentence

def count_text_info(sentence):
    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence)
    return word_count, char_count
text = input("Enter a sentence: ")
words, chars = count_text_info(text)
print("Total Words:", words)
print("Total Characters:", chars)
