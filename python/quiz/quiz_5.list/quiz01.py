def sum(a):
    b=0
    for z in range(len(a)):
        b=b+a[z]
    return b

time = int(input())
a=[]
for i in range(1,time+1):
    a.append(i)
print(a)
print(sum(a))