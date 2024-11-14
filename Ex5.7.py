def unique(input_list):
    unique_values = []
    for item in input_list:
        if item not in unique_values:
            unique_values.append(item)
    return sorted(unique_values)

number = [4, 2, 7, 4, 1, 3, 2, 5]
numbers = unique(number)
print("Unique sorted numbers:", numbers)

string = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
strings = unique(string)
print("Unique sorted strings:", strings)
