def display_unique_words():
    # Input a sentence from the user
    sentence = input("Enter a sentence: ")
    
    # Split the sentence into words
    word_list = sentence.split()
    
    # Convert all words to lowercase and use a set to get unique words
    unique_words = set(word.lower() for word in word_list)
    
    # Sort the unique words in alphabetical order
    sorted_unique_words = sorted(unique_words)
    
    # Display the unique words
    print("Unique words in alphabetical order:")
    for word in sorted_unique_words:
        print(word)

# Call the function
display_unique_words()
