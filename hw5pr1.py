import random
import time

def tortoise_move():
    """Generates the tortoise's movement based on a random integer."""
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3  # Fast plod
    elif 6 <= i <= 7:
        return 0  # Slip
    else:
        return 1  # Slow plod

def hare_move():
    """Generates the hare's movement based on a random integer."""
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        return 0  # Sleep
    elif 3 <= i <= 4:
        return 9  # Big hop
    elif 5 <= i <= 5:
        return 1  # Small hop
    elif 6 <= i <= 8:
        return 0  # Slip
    else:
        return 2  # Small plod

def race():
    """Simulates the race between the tortoise and hare."""
    tortoise_position = 0
    hare_position = 0
    print("ON YOUR MARK, GET SET")
    print("BANG !!!!!")
    print("AND THEY'RE OFF !!!!!")
    
    while tortoise_position < 70 and hare_position < 70:
        tortoise_position += tortoise_move()
        hare_position += hare_move()
    
        tortoise_position = min(tortoise_position, 70)
        hare_position = min(hare_position, 70)
        race_line = [' '] * 70

        if tortoise_position == hare_position:
            race_line[tortoise_position - 1] = "OUCH!!!"
        else:
            race_line[tortoise_position - 1] = "T"
            race_line[hare_position - 1] = "H"

        print(''.join(race_line))

        if tortoise_position >= 70 and hare_position >= 70:
            print("It's a tie!")
            return
        elif tortoise_position >= 70:
            print("TORTOISE WINS!!! YAY!!!")
            return
        elif hare_position >= 70:
            print("HARE WINS!!! Yuch.")
            return
        time.sleep(0.5)

race()
