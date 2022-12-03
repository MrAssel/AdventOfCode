import string

# Splits rucksack into two compartments equal size
def split_rucksack(rucksack:str):
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return (first_compartment, second_compartment)

# Finds common characters in two strings
def find_common_char(string_1, string_2):
    return ''.join(set(string_1).intersection(string_2))

# Genrates value for each letter
def generate_letter_mapping():
    values = {}
    for index, letter in enumerate(string.ascii_letters):
        values[letter] = index + 1
    return  values

LETTER_MAPPING = generate_letter_mapping()
input_path = r'2022\3\input'
with open(input_path) as file:
    score_part1 = 0
    score_part2 = 0
    group_counter = 0
    previous_line = ''

    for line in file:
        line = line.rstrip()
        first, second = split_rucksack(line)
        score_part1 += LETTER_MAPPING[find_common_char(first,second)]

        # Part 2 grouping by 3
        if group_counter == 0:
            group_counter += 1
            previous_line = line
        elif group_counter == 1:
            group_counter += 1
            previous_line = find_common_char(previous_line, line)
        elif group_counter == 2:
            group_counter = 0            
            score_part2 += LETTER_MAPPING[find_common_char(previous_line, line)]

        
# Print score for part 1
print(score_part1)

# Print score for part 2
print(score_part2)