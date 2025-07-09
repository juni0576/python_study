num = int(input("몇번째 피보나치까지?"))
fibo = [0,1]
for i in range(2, num):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo)