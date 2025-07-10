def pls(x, y):
    return x + y
def miu(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
num1 = int(input("분자"))
num2 = int(input("0을 제외한 분모"))
print(num1, num2, 
      pls(num1, num2), 
      miu(num1, num2), 
      mul(num1, num2), 
      div(num1, num2), sep='\n')