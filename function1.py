# function1.py
#불변형식
a = 1.2
print("a id:", id(a) )
a = 2.3 
print("a id:", id(a) )

#가변형식
lst = [1,2,3]
print("lst id:", id(lst) )
lst.append(4)
print("lst id:", id(lst) )
print(lst)

#가변형식
def change(x):
    #지역변수로 깊은 복사
    x1 = x[:]
    x1[0] = "H"
    print("change함수내부:", x1)

#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

#불변형식인데 읽기/쓰기를 하는 경우
g = 1 
def testScope(a):
    #전역변수를 맵핑
    #global g 
    g = 2 
    return g + a 

#함수 호출
print( testScope(1) ) 
print("전역변수 g:", g)

#디버깅 
#교집합 리턴하는 함수 
def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 


#호출
print( intersect("HAM", "SPAM") )

