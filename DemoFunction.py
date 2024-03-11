#Demo Function

def setValue(newValue):
    x = newValue
    print(x)


# 호출
print(setValue(5))

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(b=10))


# 지역변수와 전역변수
x = 10
def func(a):
    return a+x
print(func(1))

def func2(a):
    x = 5
    return a+x
print(func2(1))