# test_sentiment_analyzer.py

import pytest
from Sentiment_analyzer import analyze_sentiment

def test_analyze_sentiment():
    # Positive test cases
    assert analyze_sentiment("I absolutely loved the new movie! It was fantastic and amazing.") == "Positive"
    assert analyze_sentiment("What a wonderful experience at the concert.") == "Positive"
    assert analyze_sentiment("The service was excellent and the food was great!") == "Positive"
    
    # Negative test cases
    assert analyze_sentiment("I hated the food!") == "Negative"
    assert analyze_sentiment("I feel so bad about this situation.") == "Negative"
    assert analyze_sentiment("This is the worst experience I have ever had.") == "Negative"

if __name__ == "__main__":
    pytest.main()
