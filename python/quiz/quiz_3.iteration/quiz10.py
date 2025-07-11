n=int(input("몇번째까지 제곱수를 더할까?"))
sqr_pls = 0
for x in range(n+1):
    y=x**2
    sqr_pls += y
print(sqr_pls)