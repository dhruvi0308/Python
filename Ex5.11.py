alphabet = 'abcdefghijklmnopqrstuvwxyz'
def letters(string):
    l = []
    c = []
    for letter in string.lower():
        if letter in alphabet:
            if letter in l:
                index = l.index(letter)
                c[index] += 1
            else:
                l.append(letter)
                c.append(1)
                
    tuples = list(zip(l, c))
    tuples.sort()
    return tuples

panagram = "The Quick Brown Fox Jumps Over The Lazy Dog"
s = letters(panagram)
print(s)
