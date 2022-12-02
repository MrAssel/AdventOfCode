RPS_MAP = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

RPS_SCORE = {
    'R': 1,
    'P': 2,
    'S': 3,
}

# Part 1 score calculation
def calculate_score(opponent:str, player:str):
    opponent = RPS_MAP[opponent]
    player = RPS_MAP[player]
    player_score = RPS_SCORE[player]
    if opponent == player:
        return player_score + 3
    elif (opponent == 'R' and player == 'P') or (opponent == 'P' and player == 'S') or (opponent == 'S' and player == 'R'):
        return player_score + 6
    else:
        return player_score

# Calculates the move for a win 
def winning_hand(opponent:str):
    if opponent == 'R':
        return 'P'
    elif opponent == 'P':
        return 'S'
    else:
        return 'R'

# Calculates the move for a loss
def loosing_hand(opponent:str):
    if opponent == 'R':
        return 'S'
    elif opponent == 'P':
        return 'R'
    else:
        return 'P'

# Part 2 score calculation
def calculate_score_strategy(opponent:str, strategy:str):
    opponent = RPS_MAP[opponent]
    if strategy == 'X':
        return RPS_SCORE[loosing_hand(opponent)]
    elif strategy == 'Z':
        return RPS_SCORE[winning_hand(opponent)] + 6
    else:
        return RPS_SCORE[opponent] + 3

# Read each line in input
input_path = r'2022\2\input'
score_part1 = 0
score_part2 = 0
with open(input_path) as file:
     for line in file:
        score_part1 += calculate_score(line[0], line[2])
        score_part2 += calculate_score_strategy(line[0], line[2])

# Print score of part 1
print(score_part1)

# Print score of part 2
print(score_part2)