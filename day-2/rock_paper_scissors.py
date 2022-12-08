INPUT_MAP = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def read_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        inputs = [line.strip() for line in lines]

    return inputs

inputs = read_input('input.txt')

def calculate_score(inputs):
    score = 0

    for input in inputs:
        elf_input = input.split(" ")[0]
        user_input = input.split(" ")[1]

        if INPUT_MAP[user_input] == INPUT_MAP[elf_input]:
            score += (INPUT_MAP[user_input] + 3)
        elif (INPUT_MAP[user_input], INPUT_MAP[elf_input]) in [(1, 2), (2, 3), (3, 1)]:
            score += INPUT_MAP[user_input]
        else:
            score += (INPUT_MAP[user_input] + 6)
    
    return score

score = calculate_score(inputs)
print(score)

# PART 2
ROCK_OUTCOMES = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
PAPER_OUTCOMES = [('B', 'Y'), ('C', 'X'), ('A', 'Z')]
SCISSORS_OUTCOMES = [('C', 'Y'), ('A', 'X'), ('B', 'Z')]

RPS_POINTS = {"A": 1, "B": 2, "C": 3}
OUTCOME_POINTS = {"X": 0, "Y": 3, "Z": 6}

def p2_calculate_score(inputs):
    score = 0

    for input in inputs:
        elf_input = input.split(" ")[0]
        outcome_input = input.split(" ")[1]

        if (elf_input, outcome_input) in ROCK_OUTCOMES:
            score += (RPS_POINTS["A"] + OUTCOME_POINTS[outcome_input])
        elif (elf_input, outcome_input) in PAPER_OUTCOMES:
            score += (RPS_POINTS["B"] + OUTCOME_POINTS[outcome_input])
        else:
            score += (RPS_POINTS["C"] + OUTCOME_POINTS[outcome_input])

    return score

score = p2_calculate_score(inputs)
print(score)
