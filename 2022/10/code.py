from math import floor
# Define constants
CYCLES = [20,60,100,140,180,220]
CRT_LINES = [40,80,120,160,200,240]
CRT = [[],[],[],[],[],[]]

# Load data
def load_data(path:str) -> list:
    with open(path) as file:
        data = []
        for line in file:
            data.append(line.rstrip('\n').split(' '))
    return data

# Clock for incrementing cycla and CRT
def clock(cycle:int,x:int):
    calculate_CRT(cycle,x)
    return cycle + 1

# Calculate new x*cycle if in limit
def calc_cycle_x(cycle:int, x:int):
    if cycle in CYCLES: 
        return (x * cycle)
    return 0

# noop command
def command_noop(cycle:int, x:int):
    cycle = clock(cycle,x)
    sum_x = calc_cycle_x(cycle,x)
    return (cycle, sum_x)

# addx command
def command_addx(cycle:int, x:int, addx:int):
    sum_x = 0
    cycle = clock(cycle,x)
    sum_x += calc_cycle_x(cycle,x)
    cycle = clock(cycle,x)
    sum_x += calc_cycle_x(cycle,x)
    x += addx
    return cycle, sum_x, x

# Calculate CRT sign
def calculate_CRT(cycle:int, x:int):
    i = floor(cycle /40)
    if x - (cycle-40*i) <= 1 and x - (cycle-40*i) >= -1:
        CRT[i].append('#')
    else:
        CRT[i].append('.')

# Print CRT to file
def print_CRT(path):
    with open(path, 'w') as file:
        for line in CRT:
            file.write(f"{line}\n")

# Run program
def execute_program(commands:list):
    cycle = 0
    x = 1
    sum_x = 0
    for command in commands:
        if command[0] == 'noop':
            cycle, new_sum = command_noop(cycle, x)
        elif command[0] == 'addx':
            cycle, new_sum, x = command_addx(cycle, x, int(command[1]))
        sum_x += new_sum
    return sum_x

# Test
def test():
    assert execute_program(load_data(r'2022\10\test.txt')) == 13140

#test()
data = load_data(r'2022\10\input')
print(execute_program(data))
print_CRT(r'2022\10\CRT.txt')
