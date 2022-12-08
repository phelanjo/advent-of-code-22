def read_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        inputs = [line.strip() for line in lines]
    
    return inputs

def letter_to_priority_number(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return next((i+1 for i, _letter in enumerate(alphabet) if _letter == letter), None)

def get_rucksack_priorities_sum(input):
    rucksack_priorities_sum = 0
    for i in input:
        item_1, item_2 = i[:len(i)//2], i[len(i)//2:]
        common_item = ''.join(set(item_1).intersection(item_2))
        rucksack_priorities_sum += letter_to_priority_number(common_item)
    
    return rucksack_priorities_sum

input = read_input('input.txt')
rucksack_priorities_sum = get_rucksack_priorities_sum(input)

print(rucksack_priorities_sum)

# Part 2
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_badge_priorities_sum(input):
    badge_priorities_sum = 0
    for badge_group in divide_chunks(input, 3):
        elf_1, elf_2, elf_3 = badge_group
        badge_letter = ''.join(set(elf_1).intersection(elf_2).intersection(elf_3))
        badge_priorities_sum += letter_to_priority_number(badge_letter)

    return badge_priorities_sum

badge_priorities_sum = get_badge_priorities_sum(input)

print(badge_priorities_sum)