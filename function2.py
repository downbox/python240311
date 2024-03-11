# function2.py 
#기본 값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자 방식 전달
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

print(connectURI("credu.com", "80"))
print(connectURI(port="80",server="test.com"))

#가변인자(갯수가 정해져 있지 않은경우)
def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res 

print( union("HAM","SPAM") )
print( union("HAM","SPAM","EGG") )

#정의되지 않은 인자 처리
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

print( userURIBuilder("credu.com","80", 
    id="kim", name="김길동", age="30"))

#람다 함수 정의
g = lambda x,y:x*y
print("람다함수 테스트")
print( g(2,3) )
print( g(3,5) )
print( (lambda  x:x*x)(3) )
print( globals() )

#재귀호출
def factorial(x):
    """이 함수는 팩토리얼 연산을
       수행하는 함수입니다."""
    if x == 1:
        return 1 
    return x * factorial(x-1)
#호출
print( factorial(3) )
#print( help(factorial) )
print( factorial.__doc__ )

#제너레이터 패턴 함수
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

#호출
for char in reverse("abcde"):
    print(char)

#잘못 코딩한 경우 
def abc():
    s = "abc"
    for char in s:
        yield char

for item in abc():
    print(item)

lst = [1,2,3,4,5]
print( tuple(i**2 for i in lst) )
