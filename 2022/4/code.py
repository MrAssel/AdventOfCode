import pandas as pd

# Takes string and returns interval as tuples of integers
def get_interval(string:str):
    start, end = string.split('-')
    return (int(start), int(end))

# Check if two tuples fully overlap
def fully_overlap(interval_1:tuple, interval_2:tuple):
    if ((interval_1[0] >= interval_2[0] and interval_1[1] <= interval_2[1]) or
         interval_2[0] >= interval_1[0] and interval_2[1] <= interval_1[1]):
        return True
    return False

# Check if two tuples partly overlap
def partly_overlap(interval_1:tuple, interval_2:tuple):
    interval_1 = pd.Interval(interval_1[0], interval_1[1], closed='both')
    interval_2 = pd.Interval(interval_2[0], interval_2[1], closed='both')
    if interval_1.overlaps(interval_2):
        return True
    return False

input_path = r'2022\4\input'
with open(input_path) as file:
    score_part_1 = 0
    score_part_2 = 0
    for line in file:
        first_elf, second_elf = line.rstrip().split(',')
        first_elf, second_elf = get_interval(first_elf), get_interval(second_elf)
        if fully_overlap(first_elf, second_elf):
            score_part_1 += 1
        if partly_overlap(first_elf, second_elf):
            score_part_2 += 1

# Print score part 1
print(score_part_1)

# Print score part 2
print(score_part_2)
