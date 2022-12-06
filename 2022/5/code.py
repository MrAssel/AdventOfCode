import re
import numpy as np

def clean_matrix(matrix:list):
    matrix = np.rot90(np.vstack(matrix),3)
    output = []
    for array in matrix:
        output.append(list(np.delete(array, np.where(array== '    '))))
    return output

def parser(file):
    crate_matrix = []
    instructions_matrix = []
    for line in file:
        if re.findall("[A-Z,]", line):
            crate_matrix.append(re.findall("\s\s\s\s|[A-Z,]", line))
        elif re.findall("move", line):
            instructions_matrix.append(re.findall("\d+", line))

    return (clean_matrix(crate_matrix), instructions_matrix)

def move_single_crate(crate_matrix:list, instruction:list):
    from_stack = int(instruction[1])-1
    to_stack = int(instruction[2])-1
    for i in range(int(instruction[0])):
        crate_to_move = crate_matrix[from_stack][-1]
        crate_matrix[from_stack] = crate_matrix[from_stack][0:-1]
        crate_matrix[to_stack].append(crate_to_move)

    return crate_matrix

def move_multiple_crates(crate_matrix:list, instruction:list):
    n = int(instruction[0])
    from_stack = int(instruction[1])-1
    to_stack = int(instruction[2])-1
    crates_to_move = crate_matrix[from_stack][-n:]
    crate_matrix[from_stack] = crate_matrix[from_stack][0:-n]
    crate_matrix[to_stack].extend(crates_to_move)
    
    return crate_matrix

if __name__ == "__main__":
    input_path = r'2022\5\input'

    # Part 1
    with open(input_path) as file:
        crate_matrix, instruction_matrix = parser(file)

    for instruction in instruction_matrix:
        crate_matrix = move_multiple_crates(crate_matrix, instruction)

    for crate in crate_matrix:
        print(crate)

    # Part 2
    with open(input_path) as file:
        crate_matrix, instruction_matrix = parser(file)

    for instruction in instruction_matrix:
        crate_matrix = move_multiple_crates(crate_matrix, instruction)
    
    for crate in crate_matrix:
        print(crate)