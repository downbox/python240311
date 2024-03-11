# ListDict.py
# Set 형식
a = {1,2,3,3}
b = {3,4,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Tuple 형식
tp = (10,20,30)
print(len(tp))

# 함수 정의
def calc(a,b):
    return a+b, a*b, a-b

# 호출
result = calc(3,4)
print(result)

c = ("김","김유신")
print("id: %s, name: %s" % ("kim","김유신"))
print("id: %s, name: %s" % (c))

# 형식변환
t = (1,2,3)
u = list(t)
u.append(55)
print(u)

# 딕셔너리
fruits = {"apple":"red", "orange":"yellow"}
print(fruits)
print(fruits["apple"])
# print(fruits["red"])
# 입력
fruits["kiwi"] = "green"
print(fruits)
# 삭제
del fruits["apple"]
print(fruits)
print("--")
# 반복문
for item in fruits.items():
    print(item)

