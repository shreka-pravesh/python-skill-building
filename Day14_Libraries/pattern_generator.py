import itertools
def pattern_generator():
    letters = input("Enter characters (e.g., ABC): ")
    filename = "patterns.txt"
    with open(filename, 'w') as f:
        for r in range(1, len(letters) + 1):
            for combo in itertools.permutations(letters, r):
                f.write("".join(combo) + "\n")
    print(f"Patterns saved successfully to {filename}")
if __name__ == "__main__":
    pattern_generator()
