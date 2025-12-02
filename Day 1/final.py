pos = 50
count_end = 0
count_during = 0

with open(r"C:\Users\monfortel_asmilan\Downloads\Advent of Code 2025\Day 1\input.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])

        for _ in range(steps):
            if direction == "R":
                pos = (pos + 1) % 100
            else:
                pos = (pos - 1) % 100
        
            if pos == 0:
                count_during += 1

        if pos == 0:
            count_end += 1

print("PART 1 is this:", count_end)
print("PART 2 is this:", count_during)