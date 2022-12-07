def get_caloric_amounts_list_from_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        caloric_amounts = [line.strip() for line in lines]
    
    return caloric_amounts

def elf_calorie_counter(input_file):
    caloric_amounts = get_caloric_amounts_list_from_input(input_file)
    elf_caloric_sums_list = []
    current_elf_sum = 0

    for caloric_amount in caloric_amounts:
        if caloric_amount is not '':
            current_elf_sum += int(caloric_amount)
        else:
            elf_caloric_sums_list.append(current_elf_sum)
            current_elf_sum = 0
    
    elf_caloric_sums_list.append(current_elf_sum)
    
    return elf_caloric_sums_list

def top_elf_caloric_value(elf_caloric_sums):
    elf_caloric_sums.sort(reverse=True)
    return elf_caloric_sums[0]

def top_three_elves_caloric_values(elf_caloric_sums):
    elf_caloric_sums.sort(reverse=True)
    return elf_caloric_sums[0] + elf_caloric_sums[1] + elf_caloric_sums[2]

# Output
elf_caloric_sums_list = elf_calorie_counter("input.txt")

top_elf = top_elf_caloric_value(elf_caloric_sums_list)
print(top_elf)

top_three_elves = top_three_elves_caloric_values(elf_caloric_sums_list)
print(top_three_elves)
