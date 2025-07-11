def testPrime(n):
    number=2
    count =0
    while number < n:
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
maxNum=100
testPrime(maxNum)