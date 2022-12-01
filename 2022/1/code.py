input_path = r'2022\1\input'

# Sorts list with greatest values last and return the last n items
def get_n_max_values(list : list, n : int):
    list.sort()
    return list[-n:]

# Read each line in input
with open(input_path) as file:
    calorie_sum = 0
    calorie_list = []
    for line in file:
        line = line.rstrip()
        if line == '':
            calorie_list.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(line)

# Print max value 
print(max(calorie_list))

# Print sum of top 3 values
print(sum(get_n_max_values(list=calorie_list,n=3)))
