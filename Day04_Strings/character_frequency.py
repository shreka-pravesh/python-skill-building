# Count how many times each character appears in a string

def char_frequency(text):
    frequency = {}
    for char in text:
        if char != " ":  # Ignore spaces
            frequency[char] = frequency.get(char, 0) + 1
    return frequency
sentence = input("Enter a sentence: ")
result = char_frequency(sentence)
print("\nCharacter Frequency:")
for char, count in result.items():
    print(f"'{char}' appears {count} time(s)")
