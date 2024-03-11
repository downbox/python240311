# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, "문자열", 3.14]
for item in lst:
    print(item, type(item))


device = {"아이폰":5, "아이패드":10}
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)