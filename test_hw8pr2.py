import hw8pr2

def test_sum_with_digits_only():
    assert hw8pr2.sum("5 0 8 7 9 3 7 3 1 1") == 44
    assert hw8pr2.sum("1 2 3 4 5") == 15
    assert hw8pr2.sum("9 8 7") == 24
    assert hw8pr2.sum("0 0 0") == 0

def test_sum_with_words_only():
    assert hw8pr2.sum("five zero eight") == 13
    assert hw8pr2.sum("one two three") == 6
    assert hw8pr2.sum("seven six five") == 18

def test_sum_with_mixed_input():
    assert hw8pr2.sum("5 zero 3 one 2") == 11 
    assert hw8pr2.sum("four 1 2 three") == 10  
    assert hw8pr2.sum("nine 0 seven 4") == 20  
    assert hw8pr2.sum("3 Two 4") == 9 

def test_sum_with_invalid_words():
    assert hw8pr2.sum("three four eleven") == 7  
    assert hw8pr2.sum("five ten 3") == 8  

if __name__ == "__main__":
    test_sum_with_digits_only()
    test_sum_with_words_only()
    test_sum_with_mixed_input()
    test_sum_with_invalid_words()
    print("All tests passed!")
