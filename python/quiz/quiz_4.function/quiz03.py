def pls(x, y):
    return x + y
def miu(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

def calc(a,b):
    result_add=pls(a,b)
    result_miu=miu(a,b)
    result_mul=mul(a,b)
    result_div=div(a,b)
    print(f"{result_add},{result_miu},{result_mul},{result_div}")

num1 = int(input())
num2 = int(input())
calc(num1,num2)