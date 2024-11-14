def convert_word(word):
    """Convert a single word to Pig Latin."""
    if len(word) < 2:
        return word  
    
    if word[0] in 'aeiou':  
        result = word + 'ay'
    else:
        result = word[1:] + word[0] + 'ay'  
    print(f"convert_word('{word}') = '{result}'")
    return result

def convert_phrase(phrase):
    """Convert a phrase to Pig Latin."""
    words = phrase.split() 
    pig_latin_words = [convert_word(word) for word in words] 
    return ' '.join(pig_latin_words) 
if __name__ == "__main__":
    # Example usage of the functions
    phrase = input("Enter a phrase to convert to Pig Latin: ")
    pig_latin_phrase = convert_phrase(phrase)
    print(f"Pig Latin: {pig_latin_phrase}")
