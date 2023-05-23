## 함수 선언부
def add_func(n1, n2):
    result = n1 + n2
    return result

def sub_func(n1, n2):
    result = n1 - n2
    return result

def mul_func(n1, n2):
    result = n1 * n2
    return result

def div_func(n1, n2):
    result = n1 / n2
    return result

def sqr_func(n1, n2):
    result = n1 ** n2
    return result


## 전역 변수부
num1, num2, res = 16, 16, 0

## 메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)

res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)

res = mul_func(num1, num2)
print(num1, "*", num2, "=", res)

res = div_func(num1, num2)
print(num1, "/", num2, "=", res)

res = sqr_func(num1, num2)
print(num1, "^", num2, "=", res)

