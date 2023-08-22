from random import randint


def generate_numbers(n):
    num_list = [randint(1,45)]
    while len(num_list) != n :
        num = randint(1,45)
        for in_num in num_list :
            if in_num != num :
                num_list.append(num)
            break
    return num_list
    
def draw_winning_numbers():
    winning_list = generate_numbers(7)
    bonus = winning_list[(len(winning_list) - 1)]
    winning_list.remove(bonus)
    winning_list.sort()
    winning_list.append(bonus)
    return winning_list

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num_1 in numbers :
        for num_2 in winning_numbers :
            if num_1 == num_2 :
                count += 1
    return count

def check(numbers, winning_numbers):
    bonus = winning_numbers[len(winning_numbers) - 1]
    winning_numbers.remove(bonus)
    match_count = count_matching_numbers(numbers,winning_numbers)
    winning_numbers.append(bonus)
    for num in numbers :
        if bonus == num :
            bonus = True
    if match_count == 6 :
        return 1000000000
    elif match_count == 5 and bonus :
        return 50000000
    elif match_count == 5 :
        return 1000000
    elif match_count == 4 :
        return 50000
    elif match_count == 3 :
        return 5000
    else :
        return 0
