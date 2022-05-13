def prime_numbers(start_number, end_number):
    primes = []
    for number in range(start_number, end_number):
        for i in range(2, number):
            if not (number % i) == 0:
                primes.append(number)
    return primes
