# Keeps a file of prime numbers, updates the file for ever new prime number found, starts at 2 and makes file if it doesn't already exist

primes = []

# Read the list of primes from a file
try:
    with open("prime_numbers.txt", "r") as file:
        primes = [int(prime) for prime in file.read().split()]
except FileNotFoundError:
    pass

if primes:
    num1 = primes[-1] + 1
else:
    num1 = 2

while num1 <= 1000000:
    is_prime = True
    increaser = 2

    while increaser < num1:
        if num1 % increaser == 0:
            is_prime = False
            break
        increaser += 1

    if is_prime:
        primes.append(num1)
        print(num1, "is prime")

    num1 += 1

    # Update the file with the list of primes
    with open("prime_numbers.txt", "w") as file:
        file.write(" ".join(map(str, primes)))
