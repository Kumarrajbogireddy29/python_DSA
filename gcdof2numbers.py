def gcd(a,b):
    while b != 0:
        a, b = b ,a%b
    return a 

num1 = 12
num2 = 15  
print("Gcd of",num1,"and",num2,"is",gcd(num1,num2))