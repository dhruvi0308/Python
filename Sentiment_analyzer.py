positive_words = {
    "happy", "joy", "love", "wonderful", "excellent", "great", 
    "amazing", "positive", "awesome", "fantastic", "good"}

negative_words = {
    "sad", "hate", "terrible", "awful", "bad", "horrible", 
    "negative", "disappointing", "angry", "worst","hated"}

def analyze_sentiment(text):
    """Analyzes the sentiment of the input text and returns the sentiment classification."""
    text = text.lower()
    words = text.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    if positive_count > negative_count:
        return "Positive"
    if negative_count > positive_count:
        return "Negative"

if __name__ == "__main__":
    # Example usage
    input_text = input("Enter the text to analyze: ")
    sentiment = analyze_sentiment(input_text)
    print(f"The sentiment of the text is: {sentiment}")
