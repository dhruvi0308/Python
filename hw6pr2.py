import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
FACES = ['A'] + [str(number) for number in range(2, 11)] + ['J', 'Q', 'K']
NUM_FACES = 13
HAND_LENGTH = 5

def initialize_deck():
    """Create and return deck."""
    deck = []  # create an empty deck
    for suit in SUITS:  # for each suit
        for face in FACES:  # for each face (rank)
            deck.append((face, suit))  # create and append card
    return deck  # return the deck of cards (list of tuples)

def count_faces(hand):
    """Count the occurrences of each face in the hand."""
    face_count = {}
    for card in hand:
        face = card[0]
        if face in face_count:
            face_count[face] += 1
        else:
            face_count[face] = 1
    return face_count

def is_full_house(hand):
    """Returns a Boolean indicating whether hand contains a full house."""
    face_counts = count_faces(hand)
    return sorted(face_counts.values()) == [2, 3]

def is_four_of_a_kind(hand):
    """Returns a Boolean indicating whether hand contains four of a kind."""
    face_counts = count_faces(hand)
    return 4 in face_counts.values()

def is_three_of_a_kind(hand):
    """Returns a Boolean indicating whether the hand contains exactly three of a kind."""
    face_counts = count_faces(hand)
    return list(face_counts.values()).count(3) == 1 and len(face_counts) == 3

def is_two_pairs(hand):
    """Returns a Boolean indicating whether hand contains two pairs."""
    face_counts = count_faces(hand)
    return list(face_counts.values()).count(2) == 2

def is_pair(hand):
    """Returns a Boolean indicating whether hand contains a pair."""
    face_counts = count_faces(hand)
    return list(face_counts.values()).count(2) == 1 and list(face_counts.values()).count(1) == 3

def check_hand(hand):
    """Prints the hand and the returned value of your functions, useful for testing."""
    print("\n***** Your hand is:", hand, "*****")  # print the hand
    print("Hand contains a full house:", is_full_house(hand))
    print("Hand contains four of a kind:", is_four_of_a_kind(hand))
    print("Hand contains three of a kind:", is_three_of_a_kind(hand))
    print("Hand contains two pairs:", is_two_pairs(hand))
    print("Hand contains a pair:", is_pair(hand))

if __name__ == '__main__':
    deck = initialize_deck()  # create a new deck
    four_aces = deck[0::NUM_FACES]
    four_of_a_kind = four_aces + [deck[1]]  # four aces, and a ('2','Hearts)
    random.shuffle(four_of_a_kind)  # randomly shuffle this hand
    random_four_of_a_kind_tuple = tuple(four_of_a_kind)  # make a hand tuple
    check_hand(random_four_of_a_kind_tuple)
    
    random.shuffle(deck)  # randomly shuffle the initial deck
    hand = tuple(deck[:HAND_LENGTH])  # get a five-card poker hand tuple
    check_hand(hand)
