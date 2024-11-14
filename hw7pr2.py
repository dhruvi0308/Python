def are_friends(p1, p2, network):
    """ Returns whether p1 and p2 are direct friends. """
    return p2 in network.get(p1, [])

def find_common_friends(p1, p2, network):
    """ Returns a list of names that are common direct friends of p1 and p2. """
    friends_of_p1 = set(network.get(p1, []))
    friends_of_p2 = set(network.get(p2, []))
    
    return list(friends_of_p1.intersection(friends_of_p2))

def print_functions(network):
    print("Lucy and George are friends?", are_friends("Lucy", "George", network))
    print("Dan and Frank are friends?", are_friends("Dan", "Frank", network))
    print("Alex and Hanna's common friends:", find_common_friends("Alex", "Hanna", network))
    print("Ben and Dan's common friends:", find_common_friends("Ben", "Dan", network))
    print("Moa and Ben's common friends:", find_common_friends("Ben", "Moa", network))

if __name__ == '__main__':
    network = {
        "Alex": ["Ben", "Dan", "Frank"],
        "Ben": ["Alex", "Dan", "Hanna"],
        "Chris": ["George", "Lucy"],
        "Dan": ["Alex", "Ella", "Hanna", "Ben"],
        "Ella": ["Dan", "Juan"],
        "Frank": ["Alex", "Kim"],
        "George": ["Chris", "Lucy"],
        "Hanna": ["Dan", "Ben", "Kim"],
        "Juan": ["Ella"],
        "Kim": ["Frank", "Hanna"],
        "Lucy": ["Chris", "George", "Moa"],
        "Moa": ["Lucy"],
    }
    print_functions(network)

    # Additional test cases
    print("Alex and Frank's common friends:", find_common_friends("Alex", "Frank", network))
    print("Chris and Lucy's common friends:", find_common_friends("Chris", "Lucy", network))
    print("Dan and Ella are friends?", are_friends("Dan", "Ella", network))  # True

