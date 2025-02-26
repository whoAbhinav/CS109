# Roll two 6-sidex dice. What is probability the sum = 7?

import random
from tqdm import tqdm

N_TRIALS = 10000000  # getting close to infinity
TARGET_SUM = 7  # do the two dice sum to 7

def main():
    n_events = 0
    for i in tqdm(range(N_TRIALS)):
        dice_total = run_experiment()
        if dice_total == TARGET_SUM:
            n_events += 1
    pr_e = n_events / N_TRIALS
    print(f'after {N_TRIALS} trials')
    print('P(E) ≈ ', pr_e)

def run_experiment():
    d_1 = roll_dice()
    d_2 = roll_dice()
    return d_1 + d_2

def roll_dice():
    # give me a random dice roll
    # alternatively random.randint(1, 7)
    return random.choice([1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    # this starts the program in main
    main()
