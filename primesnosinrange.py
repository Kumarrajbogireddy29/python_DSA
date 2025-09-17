def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example: find primes between 10 and 50
start, end = 10, 50
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")