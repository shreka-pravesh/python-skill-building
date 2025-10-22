def word_frequency(filename):
    try:
        with open(filename, "r") as f:
            text = f.read().lower().split()
            freq = {}
            for word in text:
                freq[word] = freq.get(word, 0) + 1
            print("\n=== Word Frequency ===")
            for word, count in freq.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found!")
if __name__ == "__main__":
    word_frequency("sample.txt")
