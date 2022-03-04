import random

def roll(die_sides,rolls=1):
    '''
    Takes number of sides of the die as the first argument, and number of rolls as the second optional argument.
    Returns results in the form of a list.

    example:
        roll_die(6) will roll a six sided die once.
        roll_die(20,3) will roll a twenty sided die three times.
    '''
    answer = []
    for i in range(rolls):
        answer += [random.choice(range(1,die_sides+1))]
    return answer
