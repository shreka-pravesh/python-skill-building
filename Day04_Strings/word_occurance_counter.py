# Count how many times each word appears in a sentence

def word_occurrence(sentence):
    words = sentence.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
text = input("Enter a sentence: ")
result = word_occurrence(text)
print("\nWord Occurrences:")
for word, freq in result.items():
    print(f"'{word}' appears {freq} time(s)")
