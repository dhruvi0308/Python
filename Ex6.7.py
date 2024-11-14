sentence = input("Please enter a sentence: ")
letter_count = {}

for char in sentence.lower():
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

sorted_letters = sorted(letter_count.keys())

print(f"{'Letter':<10} {'Count':<10}")

for letter in sorted_letters:
    print(f"{letter:<10} {letter_count[letter]:<10}")
