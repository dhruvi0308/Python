words = ["listen", "silent", "enlist", "rat", "tar", "god", "dog", "art"]

anagrams = {}

for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]

print(anagrams)
