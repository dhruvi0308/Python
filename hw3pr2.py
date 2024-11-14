def compute_largest_factor(number):
    '''For the given positive number, the function computes and returns its largest factor.'''
    largest_factor = 1 
    for i in range(1, number):
        if number % i == 0:
            largest_factor = i
    return largest_factor

if __name__ == '__main__':
    for x in [10, 7, 12345, 54321]:
        print(compute_largest_factor(x))
