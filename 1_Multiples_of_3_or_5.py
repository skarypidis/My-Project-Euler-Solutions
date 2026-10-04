multiples_of_3 = [3]
multiples_of_5 = [5]
multiples_of_3_and_5 = []

def all_multiples_of_3():
    current_multiple_3 = 3
    n = 2
    while current_multiple_3 < 999:
        next_multiple_3 = 3 * n
        multiples_of_3.append(next_multiple_3)
        current_multiple_3 = next_multiple_3
        n += 1
    return sum(multiples_of_3)

def all_multiples_of_5():
    current_multiple_5 = 5
    n = 2
    while current_multiple_5 < 995:
        next_multiple_5 = 5 * n
        multiples_of_5.append(next_multiple_5)
        current_multiple_5 = next_multiple_5
        n += 1
    return sum(multiples_of_5)

def remove_double_counting():

    all_multiples_of_5()
    all_multiples_of_3()

    merged_list = multiples_of_3 +multiples_of_5
    merged_list_no_double_counting = list(set(merged_list))
    return sum(merged_list_no_double_counting)

print(remove_double_counting())