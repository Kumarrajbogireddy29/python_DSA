def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

# Example
num1 = 12
num2 = 25

if are_coprime(num1, num2):
    print(num1, "and", num2, "are co-prime")
else:
    print(num1, "and", num2, "are NOT co-prime")
