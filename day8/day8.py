import string
from typing import List, Dict


def read_input():
    return [(l.strip().split(" | ")[0].split(" "), l.strip().split(" | ")[1].split(" ")) for l in
            open("data/day8.txt", "r").readlines()]


def part_one(lines):
    print(sum(len(list(filter(lambda x: x in [2, 3, 7, 4], map(len, l[1])))) for l in lines))


def revert_dict(d): return {v: k for k, v in d.items()}


digit_by_segment = revert_dict(
    {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6: 'abdefg', 7: 'acf',
     8: 'abcdefg', 9: 'abcdfg'})


# Return all string of l with length equals to n
def filter_str_list_by_len(l, n) -> List:
    return [x for x in l if len(x) == n]


# Remove all char of to_remove from s
def remove_char(s: str, to_remove: str):
    return "".join([c for c in s if c not in to_remove])


# Return all string from l containing all char from s
def get_containing(l: List[str], s: str) -> List:
    return [s_ for s_ in l if remove_char(s, s_) == ""]


# Replace char in s according to the dict mapping
def decode(s: str, mapping: Dict[str, str]) -> str:
    return "".join([mapping[c] for c in s])


def get_mapping(l: List[str]) -> Dict[str, str]:
    mapping = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
    one = filter_str_list_by_len(l, 2)[0]
    vor = filter_str_list_by_len(l, 4)[0]
    seven = filter_str_list_by_len(l, 3)[0]
    eight = filter_str_list_by_len(l, 7)[0]

    l.remove(one)
    l.remove(vor)
    l.remove(seven)
    l.remove(eight)

    cf = one
    mapping["a"] = remove_char(seven, one)
    bd = remove_char(vor, one)

    nine = sorted(get_containing(l, cf + bd + mapping["a"]), key=len)[0]
    l.remove(nine)

    mapping["e"] = remove_char(eight, nine)

    # on essaie de déterminer cf
    # si on enlève le segment c ça nous donne 6 alors que le f ne donne rien
    case_1 = get_containing(l, remove_char(eight, cf[0]))
    case_2 = get_containing(l, remove_char(eight, cf[1]))

    if len(case_1) == 1:
        mapping["c"] = cf[0]
        mapping["f"] = cf[1]
        six = case_1[0]
    else:
        mapping["c"] = cf[1]
        mapping["f"] = cf[0]
        six = case_2[0]

    l.remove(six)

    # il manque encore 0, 2, 3, 5
    # 0 est le seul qui a 6 segment
    zero = filter_str_list_by_len(l, 6)[0]
    l.remove(zero)

    mapping["d"] = remove_char(eight, zero)
    mapping["b"] = remove_char(bd, mapping["d"])

    # seules 2 segment ne sont pas utilisé par ni 4, ni 1 ni 7 (e et g)
    eg = remove_char(remove_char(remove_char(eight, vor), one), seven)

    mapping["g"] = remove_char(eg, mapping["e"])

    assert set(mapping.keys()) == set(mapping.values())

    return revert_dict(mapping)


def part_two(lines):
    numbers = list()
    for l in lines:
        mapping = get_mapping(l[0])
        number_s = ""
        for code in l[1]:
            segments = sorted(decode(code, mapping))
            number_s += str(digit_by_segment["".join(segments)])
        numbers.append(int(number_s))

    print(sum(numbers))


if __name__ == "__main__":
    part_one(read_input())
    part_two(read_input())
