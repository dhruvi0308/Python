import pytest
from Anagram_checker import are_anagrams

def test_are_anagrams():
    assert are_anagrams("race", "care") == True
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("apple", "pale") == False
    assert are_anagrams("Hello", "O hell") == True
    assert are_anagrams("", "") == True
    assert are_anagrams("Dormitory", "Dirty room") == True
    assert are_anagrams("The eyes", "They see") == True
    assert are_anagrams("Anagram", "Nagaram") == True
    assert are_anagrams("Not an anagram", "An anagram ton") == True

if __name__ == "__main__":
    pytest.main()
