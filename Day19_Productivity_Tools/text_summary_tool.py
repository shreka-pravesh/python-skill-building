import re
from collections import Counter
def tokenize_sentences(text):
    # split on sentence punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]
def tokenize_words(text):
    # simple word tokenizer, lowercase, remove non-alphanumerics
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    return words
def score_sentences(sentences, freq):
    scores = {}
    for s in sentences:
        words = tokenize_words(s)
        if not words:
            scores[s] = 0
            continue
        scores[s] = sum(freq.get(w, 0) for w in words) / len(words)
    return scores
def summarize(text, max_sentences=2):
    sentences = tokenize_sentences(text)
    if len(sentences) <= max_sentences:
        return sentences
    words = tokenize_words(text)
    freq = Counter(words)
    # normalize frequencies
    max_f = max(freq.values()) if freq else 1
    for w in list(freq):
        freq[w] = freq[w] / max_f
    scores = score_sentences(sentences, freq)
    # pick top sentences preserving original order
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    selected = set(s for s, _ in ranked[:max_sentences])
    summary = [s for s in sentences if s in selected]
    return summary
def main():
    print("=== Text Summary Tool ===")
    print("Paste a paragraph (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    paragraph = "\n".join(lines).strip()
    if not paragraph:
        print("No input provided.")
        return
    n = input("How many sentences for summary? (default 2): ").strip()
    try:
        n = int(n) if n else 2
    except ValueError:
        n = 2
    summary = summarize(paragraph, max_sentences=n)
    print("\n--- Summary ---")
    for s in summary:
        print(s)
    print("----------------")
if __name__ == "__main__":
    main()
