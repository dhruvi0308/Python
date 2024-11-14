def count_family(names):
    """ Returns a dictionary with keys being the unique last names and
    values being the number of times each last name appears in the list. """
    family_count = {}
    
    for full_name in names:
        last_name = full_name.split()[-1]
        if last_name in family_count:
            family_count[last_name] += 1
        else:
            family_count[last_name] = 1
            
    return family_count

def count_initials(names):
    """ Returns a dictionary with the numbers of names with the same initials. """
    initials_count = {}
    
    for full_name in names:
        first_name, last_name = full_name.split()
        initials = first_name[0] + last_name[0]
        if initials in initials_count:
            initials_count[initials] += 1
        else:
            initials_count[initials] = 1
            
    return initials_count

def most_frequent_lastname(names):
    """ Returns a dictionary of the most frequent last name. """
    family_counts = count_family(names)
    most_frequent = max(family_counts, key=family_counts.get)
    return {most_frequent: family_counts[most_frequent]}

def print_functions(names):
    print("count_family:", count_family(names))
    print("count_initials:", count_initials(names))
    print("most_frequent_lastname:", most_frequent_lastname(names))

if __name__ == '__main__':
    names_test_case_1 = ["Alex Foo", "Ben Bar", "Chris Foo", "Zella Brown", "Allen Fow", "Bob Foo", "Zoe Boo"]
    print_functions(names_test_case_1)
    
    # Additional test cases
    names_test_case_2 = ["John Doe", "Jane Doe", "Alice Smith", "Bob Brown"]
    print_functions(names_test_case_2)
    
    names_test_case_3 = ["Tom Hanks", "Tom Cruise", "Brad Pitt", "Bradley Cooper", "Brad Pitt"]
    print_functions(names_test_case_3)

