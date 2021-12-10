import time
from enum import Enum
from typing import Tuple, Optional


class LineState(Enum):
    CORRUPTED = 0
    INCOMPLETE = 1
    CORRECT = 2


opening = "({[<"
closing = ")}]>"
map_score_corrupted = {")": 3, "]": 57, "}": 1197, ">": 25137}
map_score_incomplete = {")": 1, "]": 2, "}": 3, ">": 4}


def read_input():
    return [x.strip() for x in open("data/day10.txt", "r").readlines()]


def get_line_state(line: str, verbose=False) -> Tuple[LineState, Optional[str]]:
    opened_history = []
    for c in line:
        # if it is an opening char, we add it to the opened history
        if c in opening:
            opened_history.append(c)
        # if the opened_history is empty, but we encounter a closed char OR
        # if it is a closing char AND it does not correspond to the last opened char -> corrupted !
        elif len(opened_history) == 0 or opening[closing.index(c)] != opened_history[-1]:
            if verbose: print(f"Expected {closing[opening.index(opened_history[-1])]}, but found {c} instead.")
            return LineState.CORRUPTED, c  # closing trop tôt
        # if it is a closing char but it does correspond to the last opened char, we pop the last opened char from history
        else:
            opened_history.pop()

    # if it remains some non closed char at the end, we can backtrack what char are needed to terminate the sequence
    if len(opened_history) > 0:
        return LineState.INCOMPLETE, "".join([closing[opening.index(c)] for c in reversed(opened_history)])
    # if it remains no char in the history, it means we have a correct sequence
    else:
        return LineState.CORRECT, None


def part_one_two(lines):
    score_corrupted = 0
    score_incomplete = list()
    for l in lines:
        state, s = get_line_state(l)
        if state == LineState.CORRUPTED:
            score_corrupted += map_score_corrupted[s]
        elif state == LineState.INCOMPLETE:
            score = 0
            for c in s:
                score = score * 5 + map_score_incomplete[c]
            score_incomplete.append(score)

    print(score_corrupted)
    if len(score_incomplete) > 0:
        print(sorted(score_incomplete)[int(len(score_incomplete) / 2)])
    else:
        print("No incomplete sequence")


if __name__ == "__main__":
    t0 = time.time()
    part_one_two(read_input())
    t1 = time.time()
    print("total {total}ms".format(total=t1 - t0))
