def read_input():
    return [(l.strip().split(" ")[0], int(l.strip().split(" ")[1])) for l in open('input.txt', 'r').readlines()]


def part_one(cmds):
    pos = (0, 0)
    for cmd in cmds:
        if cmd[0] == "forward":
            pos = (pos[0] + cmd[1], pos[1])
        elif cmd[0] == "up":
            pos = (pos[0], pos[1] - cmd[1])
        elif cmd[0] == "down":
            pos = (pos[0], pos[1] + cmd[1])
        else:
            print("Unknown command")

    print(pos[0] * pos[1])


def part_two(cmds):
    pos = (0, 0)
    aim = 0
    for cmd in cmds:
        if cmd[0] == "down":
            aim += cmd[1]
        elif cmd[0] == "up":
            aim -= cmd[1]
        elif cmd[0] == "forward":
            pos = (pos[0] + cmd[1], pos[1] + aim * cmd[1])
        else:
            print("Unknown command")
    print(pos[0] * pos[1])


if __name__ == "__main__":
    part_one(read_input())
    part_two(read_input())
