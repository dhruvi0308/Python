number_words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

operation_words = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "divided by": "/"
}
def tokenize(expression):
    tokens = []
    words = expression.lower().split()
    
    i = 0
    while i < len(words):
        if words[i] == "divided" and i + 1 < len(words) and words[i + 1] == "by":
            tokens.append("/")
            i += 2

        elif words[i] in number_words:
            tokens.append(number_words[words[i]])
            i += 1

        elif words[i] in operation_words:
            tokens.append(operation_words[words[i]])
            i += 1
        else:
            i += 1
    return tokens

def calculate_expression(expression):
    tokens = tokenize(expression)
    
    if len(tokens) == 3 and isinstance(tokens[0], int) and isinstance(tokens[2], int) and tokens[1] in "+-*/":
        num1, operation, num2 = tokens
        try:
            result = eval(f"{num1} {operation} {num2}")
            return f"The result of '{expression}' is: {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid input. Please ensure you're using numbers between zero and nine, and valid operations."

while True:
    user_input = input("Enter a mathematical expression: ")
    
    print(calculate_expression(user_input))
