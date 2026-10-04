
first_term = 0
second_term = 1
def fibonacci_sequence():
    second_last_term = (first_term)
    last_term = (second_term)
    even_numbers_in_sequence = []
    while last_term < 4000000:
        new_term = second_last_term + last_term
        if (new_term/2).is_integer() and new_term < 4000000:
            even_numbers_in_sequence.append(new_term)
        second_last_term = last_term
        last_term = new_term
    return sum(even_numbers_in_sequence)

print(fibonacci_sequence())


    
