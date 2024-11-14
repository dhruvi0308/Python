from collections import Counter
sentence = input("Enter a sentence:").lower()

words = sentence.split()

word_count = Counter(words)
print(word_count)

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Duplicate words:")
for word, count in word_count.items():
    if count > 1:
        print(f"{word}: {count}")
