count_invalids_total = 0
list_invalids = []
def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
        global count_invalids_total
        count_invalids_total += 1
        list_invalids.append(s)
    return s[:mid] == s[mid:]

with open(r"C:\Users\monfortel_asmilan\Downloads\Advent of Code 2025\Day 2\input.txt") as f:
    lines = f.readlines()

total = 0

for line in lines:
    ranges = line.strip().split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid_id(i):
                total += i

print(total)
print("Total invalid IDs found:", count_invalids_total)
print("List of invalid IDs:", list_invalids)