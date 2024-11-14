import hw8pr1 as piglatin

def test_words_starting_with_vowel():
   
    assert piglatin.convert_word("all") == "allay"
    assert piglatin.convert_word("eggs") == "eggsay"
    assert piglatin.convert_word("is") == "isay"
    assert piglatin.convert_word("open") == "openay"
    assert piglatin.convert_word("under") == "underay"

def test_words_starting_with_consonant():
    
    test_words = ("be", "clark", "dog", "fish", "grape", "hat", "kite", "lamp", "moon", "nest", "quilt", "rock", "snake", "tree", "vase", "wheat", "yarn", "zebra")
    expected_results = ("ebay", "larkcay", "ogday", "ishfay", "rapegay", "athay", "itekay", "amplay", "oonmay", "estnay", "uiltqay", "ockray", "nakesay", "reetay", "asevay", "heatway", "arnyay", "ebrazay")
    
    for i in range(len(test_words)):
        assert piglatin.convert_word(test_words[i]) == expected_results[i]

def test_phrase():
   
    assert piglatin.convert_phrase("end") == "enday"
    assert piglatin.convert_phrase("let all eggs be cracked") == "etlay allay eggsay ebay rackedcay"
    assert piglatin.convert_phrase("open the door") == "openay hetay oorday"
    assert piglatin.convert_phrase("is this working") == "isay histay orkingway"
    assert piglatin.convert_phrase("the big cat") == "hetay igbay atcay"


if __name__ == "__main__":
    test_words_starting_with_vowel()
    test_words_starting_with_consonant()
    test_phrase()
    print("All tests passed!")
