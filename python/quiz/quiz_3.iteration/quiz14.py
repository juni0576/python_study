#14번 답
# while 풀이
maxNum=20
number=2
count =0

while number < maxNum:
    divisor=2
    prime=True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        count += 1
        print(number, end=' ')
    number += 1
print("\n")


# for 풀이
maxNum=20
number=2
count =0

#while number < maxNum:
for i in range(2, maxNum+1):
    divisor=2
    prime=True

    # while divisor < number:
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break
        # divisor += 1
    if prime:
        count += 1
        print(number, end=' ')
    number += 1

print("\n")

# 코파일럿 풀이
for x in range(2, 20):
    is_prime = True
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        print(x, end=' ')
print("\n")

#조경원님 풀이
for i in range(2,21):
    for j in range(1,i+1):
        if j!=1 and j!=i:
            if i%j==0:
                break
            elif i==j:
                print(j, end=' ')