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
