total_sum=0
myList=[]
for x in range(1,100):
    if x%3 ==0:
            myList.append(x)
    else:
        pass
for y in range(len(myList)):
            total_sum += myList[y]


print(myList)
print(total_sum)