def grain_weight(board_size):

    grains_per_square = 1
    weight_per_grain = 0.0115
    
    num_squares = board_size * board_size
    
    total_grains = 0
    grains = grains_per_square
    for i in range(num_squares):
        total_grains += grains
        grains *= 2
    
    total_weight_grams = total_grains * weight_per_grain
    
    grams_per_ton = 1000 * 1000
    tons = total_weight_grams / grams_per_ton
    
    return tons


if __name__ == '__main__':
    for x in [5, 8, 10]:
        print(grain_weight(x))