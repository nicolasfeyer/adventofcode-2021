from collections import Counter

import numpy as np


def read_input():
    return np.array([int(x) for x in next(open("data/day6.txt", "r")).split(",")])


# https://dev.to/qviper/advent-of-code-python-solution-day-6-22hl
def part_two(fishes_state, days=80):
    count = Counter(fishes_state)
    for _ in range(days):
        # -- Slide count of fish to the previous time key. If
        count = {l: (0 if count.get(l + 1) is None else count.get(l + 1)) for l in range(-1, 8)}

        # -- Add new born fish
        count[8] = count[-1]

        # -- Reset fish who gave life
        count[6] += count[-1]

        # -- Reset exhausted lifes
        count[-1] = 0
    print(sum(count.values()))


def part_one(fishes_state, i=0, days=80):
    if i == days:
        return print(len(fishes_state))

    # -- First mask the zeros
    ready_to_give_birth_mask = fishes_state == 0

    # --- Replace 0 by 6
    fishes_state[ready_to_give_birth_mask] = 6

    # -- Decrease other than old zero (new 6)
    fishes_state[~ready_to_give_birth_mask] -= 1

    # -- Create new array of size = original + new born
    fishes_state_ = np.ones(len(fishes_state) + ready_to_give_birth_mask.sum()) * 8

    # -- Replace with the value of the old array
    fishes_state_[:fishes_state.size] = fishes_state
    fishes_state = fishes_state_

    # -- Recursive call
    part_one(fishes_state, i + 1, days)


if __name__ == "__main__":
    part_one(read_input(), 0, 80)
    part_two(read_input(), 256)
