import re

# Load data from input
def load_data(input_path:str) -> list:
    with open(input_path) as file:
        matrix = []
        for line in file:
            row = re.findall('\d',line)
            matrix.append(row)
        return matrix

# Check if index is on edge of matrix
def is_edge(matrix:list, row_index:int, col_index:int) -> bool:
    if (row_index == 0 or col_index == 0 or 
        row_index == len(matrix[0])-1 or 
        col_index == len(matrix)-1):
        return True
    return False

# Split matrix into four list related to index position
def get_partial_lists(matrix:list, row_index:int, col_index:int) -> tuple:
    transposed_matrix = list(map(list,zip(*matrix)))
    left_list = matrix[row_index][:col_index]
    right_list = matrix[row_index][col_index+1:]
    up_list = transposed_matrix[col_index][:row_index]
    down_list = transposed_matrix[col_index][row_index+1:]
    return (left_list[::-1],right_list,up_list[::-1],down_list)

# Check if tree is visible
def is_visible(matrix:list, row_index:int, col_index:int) -> bool:
    if is_edge(matrix=matrix, row_index=row_index, col_index=col_index):
        return True

    value = matrix[row_index][col_index]
    left_list,right_list,up_list,down_list = get_partial_lists(matrix,row_index,col_index)

    if (max(left_list) >= value and
        max(right_list) >= value and
        max(up_list) >= value and
        max(down_list) >= value):
        return False

    return True

# Returns number of visible trees
def get_visible_trees(matrix:list) -> int:
    visible = 0
    for row_index in range(len(matrix[0])):
        for col_index in range(len(matrix)):
            if is_visible(matrix,row_index,col_index):
                visible += 1
    return visible

# Calculates scenic score from list
def calculate_scenic_score_from_list(lst:list, value:int) -> int:
    return next((x+1 for x, val in enumerate(lst)if val >= value),len(lst))

# Calculates scenic score for a index in a matrix
def calculate_scenic_score_from_matrix(matrix:list, row_index:int, col_index:int) -> int:
    left_list,right_list,up_list,down_list = get_partial_lists(matrix,row_index,col_index)
    value = matrix[row_index][col_index]
    score_left = calculate_scenic_score_from_list(left_list,value)
    score_right = calculate_scenic_score_from_list(right_list,value)
    score_up = calculate_scenic_score_from_list(up_list,value)
    score_down = calculate_scenic_score_from_list(down_list,value)
    return score_left * score_right * score_up * score_down

# Returns highes scentic score in matrix
def get_highest_scenic_score(matrix:list) -> int:
    score_list = []
    for row_index in range(len(matrix[0])):
        for col_index in range(len(matrix)):
            score_list.append(calculate_scenic_score_from_matrix(matrix,row_index,col_index))
    return max(score_list)

# Test if solution is correct
def test(matrix:list) -> None:
    assert get_visible_trees(matrix) == 21
    assert get_highest_scenic_score(matrix) == 8
    
# Test part 1 and 2
test_matrix = load_data(r'2022\8\test.txt')
test(test_matrix)
# Load matrix
tree_matrix = load_data(r'2022\8\input')
# Part 1
print(get_visible_trees(tree_matrix))
# Part 2
print(get_highest_scenic_score(tree_matrix))
    


