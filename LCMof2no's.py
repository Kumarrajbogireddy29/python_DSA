def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = 12
num2 = 15

print("Lcm of", num1, "and", num2, "is", lcm(num1, num2))
