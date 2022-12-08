def read_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        inputs = [line.strip() for line in lines]
    
    return inputs

def letter_to_priority_number(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return next((i+1 for i, _letter in enumerate(alphabet) if _letter == letter), None)

def get_rucksack_priorities_sum(inputs):
    rucksack_priorities_sum = 0
    for input in inputs:
        item_1, item_2 = input[:len(input)//2], input[len(input)//2:]
        common_item = ''.join(set(item_1).intersection(item_2))
        rucksack_priorities_sum += letter_to_priority_number(common_item)
    
    return rucksack_priorities_sum

inputs = read_input('input.txt')
rucksack_priorities_sum = get_rucksack_priorities_sum(inputs)

print(rucksack_priorities_sum)