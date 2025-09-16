def divisiors(n):
    divs = []
    for i in range(1,n+1):
        if n % i == 0:
            divs.append(i)
    return divs

num = 36
print("divisiors of " , num , "are" , divisiors(num))