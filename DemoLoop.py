#DemoLoop.py

value=5
while value > 0:
    print(value)
    value -= 1

print("---for in---")
lst = [100,3.14,"demo"]
for item in lst:
    print(item)

print("----range() 함ㅅ-----")
years=list(range(2000,2025))
print(years)
days = list(range(1,32))
print(days)

print("----리스트 컴프리헨션-----")
lst=list(range(1,11))
print(lst)
print([i**2 for i in lst if i > 5])
tp=("apple","kiwi")
print([len(i) for i in tp])
d={100:"apple",200:"kiwi"}
print([v.upper() for v in d.values()])

print("===필터링 사용====")
lst = [10,20,30]
iterL=filter(None, lst)
for item in iterL:
    print(item)

print("===피러링 함수 사용")
def getBiggerThan20(i):
    return i > 20

iter=filter(getBiggerThan20,lst)
for item in iter:
    print(item)

print("===람다 함수 사용")
iter=filter(lambda x:x>20, lst)   
for item in iter:
    print(item)