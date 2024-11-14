def find_ed_words(text):
    # Split the text into words based on spaces
    words = text.split()
    
    # Filter words that end with 'ed'
    ed_words = [word for word in words if word.endswith('ed')]
    
    return ed_words

# Input from the user
text = input("Enter a line of text: ")
ed_words = find_ed_words(text)

# Output the words ending with 'ed'
print("Words ending with 'ed':", ed_words)
