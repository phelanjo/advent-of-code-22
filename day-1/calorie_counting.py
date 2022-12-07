# Part 1
def get_caloric_amounts_list_from_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        caloric_amounts = [line.strip() for line in lines]
    
    return caloric_amounts

def elf_calorie_counter(input_file):
    caloric_amounts = get_caloric_amounts_list_from_input(input_file)
    current_elf_sum = 0
    top_elf_sum = 0

    for caloric_amount in caloric_amounts:
        if caloric_amount is not '':
            current_elf_sum += int(caloric_amount)
        else:
            if current_elf_sum > top_elf_sum:
                top_elf_sum = current_elf_sum
                current_elf_sum = 0
            else:
                current_elf_sum = 0
    
    return top_elf_sum

top_elf_calories = elf_calorie_counter(input_file="input.txt")
print(top_elf_calories)

