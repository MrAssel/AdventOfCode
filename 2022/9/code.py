# Define constans for clearity
X = 0
Y = 1

# Load data
def load_data(path:str) -> list:
    with open(path) as file:
        data = []
        for line in file:
            line = line.rstrip('\n').split(' ')
            data.append((line[0],int(line[1])))
    return data

# Move one knot, probably could do this nicer
def move_knot(pos_list:list) -> tuple:
    for i in range(1,len(pos_list)):
        x_diff = pos_list[i-1][X] - pos_list[i][X]
        y_diff = pos_list[i-1][Y] - pos_list[i][Y]
        if x_diff == 0 and y_diff > 1: # UP
            pos_list[i][Y] += 1
        elif x_diff > 1 and y_diff == 0: # RIGHT
            pos_list[i][X] += 1
        elif x_diff == 0 and y_diff < -1: # DOWN
            pos_list[i][Y] -= 1
        elif x_diff < -1 and y_diff == 0: # LEFT
            pos_list[i][X] -= 1
        elif ((x_diff > 0 and y_diff > 1) or # Diagonal UR
              (x_diff > 1 and y_diff > 0)):
            pos_list[i][X] += 1
            pos_list[i][Y] += 1
        elif ((x_diff < 0 and y_diff < -1) or # Diagonal DL
              (x_diff < -1 and y_diff < 0)):
            pos_list[i][X] -= 1
            pos_list[i][Y] -= 1
        elif ((x_diff > 0 and y_diff < -1) or # Diagonal DR
              (x_diff > 1 and y_diff < 0)):
            pos_list[i][X] += 1
            pos_list[i][Y] -= 1
        elif ((x_diff < 0 and y_diff > 1 ) or  # Diagonal UL
              (x_diff < -1 and y_diff > 0)):
            pos_list[i][X] -= 1
            pos_list[i][Y] += 1

    return pos_list

# Move rope
def move_rope(command:tuple, pos_list:list) -> tuple:
    tail_list = []
    for i in range(0,command[1]):
        pos_list[0][X] += {'R':1, 'L':-1}.get(command[0], 0)
        pos_list[0][Y] += {'D':-1, 'U':1}.get(command[0], 0)

        pos_list = move_knot(pos_list)
        tail_list.append(tuple(pos_list[-1]))
    return tail_list, pos_list

# Calculate last knot or "tail" of ropes unique positions
def calculate_tail_visited_pos(commands:list, pos_list:list) -> list:
    pos_visited = []
    for command in commands:
        tail_list, pos_list = move_rope(command,pos_list)
        pos_visited.extend(tail_list)
    return set(pos_visited)

# Generates a list of coordinates for each knot
def generate_start_pos(rope_length:int) -> list:
    start_pos = []
    for i in range(0,rope_length):
        start_pos.append([0,0])
    return start_pos

# Test
def test():
    assert len(calculate_tail_visited_pos(load_data(r'2022\9\test.txt'),generate_start_pos(2))) == 13
    assert len(calculate_tail_visited_pos(load_data(r'2022\9\test2.txt'),generate_start_pos(10))) == 36

# Test
test()
# Part 1
print(len(calculate_tail_visited_pos(load_data(r'2022\9\input'),generate_start_pos(2))))
# Part 2
print(len(calculate_tail_visited_pos(load_data(r'2022\9\input'),generate_start_pos(10))))