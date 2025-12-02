count_invalids_total = 0
list_invalids = []


def is_invalid_id(n: int):
    s = str(n)
    length = len(s)

    for block_size in range(1, length // 2 + 1): #rangge is xclusive of last numb (1 to 4 gives 1,2,3), added +1 to get number after block size

        if length % block_size != 0: # can the group or block selected (single, pair, double, triple, etc) it be divisible inside the large number with no remainder?
            continue 

        block = s[:block_size] # the block from the string (eg. if block size is 2, and string is 1212, block is 12),  line is taking the first blocck_size characters from the string s
        repeat_count = length // block_size # how many times the block should repeat to form the original string
        rebuilt = block * repeat_count # reconstruct the string by repeating the block repeat_count times (if the block was 12 and repeat_count was 2, rebuilt would be 1212)

        if rebuilt == s: # check if the reconstructed string matches the original string, if it does, it's invalid, means that it repeated more than twice
            global count_invalids_total
            count_invalids_total += 1
            list_invalids.append(s)
            return True

    return False

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
