def sum(number):
    """Compute the sum of digits in a string of mixed words and digits."""

    word_to_digit = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }


    tokens = number.split()
    
    total_sum = 0
    
    for token in tokens:
        if token.isdigit():  
            total_sum += int(token)
        else:  
            total_sum += word_to_digit.get(token.lower(), 0)  

    return total_sum

if __name__ == "__main__":
    # Example usage of the function
    number_string = input("Enter the phone number string: ")
    result = sum(number_string)
    print(f"The sum of the digits is: {result}")
