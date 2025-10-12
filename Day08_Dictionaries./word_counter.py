# Program: Word Counter
# Concept: Dictionary counting

text = input("Enter a sentence:\n").lower().split()
count = {}
for word in text:
    count[word] = count.get(word, 0) + 1
print("\n Word Frequency:")
for w, c in count.items():
    print(f"{w}: {c}")
