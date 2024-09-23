# function1.py

#함수정의
def setValue(newValue):
    #지역변수
    x=newValue
    print("지역변수:", x)
#함수 호출
retValue=setValue(10)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))

#교집합 문자 리턴
def intersect(prelist,postlist):
    #지역변수(LIST  )
    result=[]
    #H(0) | A(1) | M(2)
    for x in prelist:
        #만약에 X가 postlist 에 있고 x가 아직 result에 없다면 추가
        if x in postlist and x not in result:
           result.append(x)
    return result

print (intersect("HAM","SPAM"))

#기본값을 명시
def times(a=10,b=20):
    return a*b
#호출
print(times())
print(times(5))
print(times(5,6))

#지역변수와 전역변수333
x=5
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=1
    return a+x
print(func2(1))

#가변인자 함수
def union(*ar):
    #지역변수
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))
            