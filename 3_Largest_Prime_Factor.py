import math

def prime_factorise():
    subject = 600851475143
    prime_factors_of_subject = []
    #only need to test up to square root of subject 
    square_root_subject = math.sqrt(subject)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for i in primes:
        while i < square_root_subject:
            current_non_prime_factor = []
            check_factor = subject / i
            if check_factor.is_integer():
                prime_factors_of_subject.append(i)
            current_non_prime_factor = check_factor
    return prime_factors_of_subject


print(prime_factorise())