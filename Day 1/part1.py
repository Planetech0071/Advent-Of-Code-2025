pos = 50
count = 0

with open(r"C:\Users\monfortel_asmilan\Downloads\Advent of Code 2025\Day 1\input.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])

        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

        if pos == 0:
            count += 1

print("PART 1 is this:", count)