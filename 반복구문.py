# 반복구문.py

print("----while 루프----")

value = 5

while value > 0 :
    print(value)
    value -= 1

    
print("----for~ in~ 루프----")
for i in [1,2,3]:
    print(i)


print("----딕셔너리----")
d = {"name":"전우치", "age":30, "addr":"선릉역"}
for item in d.items():
    print(item)


print("----RANGE 함수----")
print(list(range(2000, 2027)))
print(list(range(1,32)))
print(list(range(1,11,2)))
for i in range(5):
    print(i)
    
print("----LIST COMPREHENSION 함수----")
lst = list(range(1,11))
print( [i**2 for i in lst if i>5])
tp = ["apple","kiwi"]
print( [len(i) for i in tp])
d = {100:"apple",200:"kiwi"}
print([v.upper() for v in d.values()])

print("----FILTER----")
lst = [10, 25, 30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

print("----FILTER 함수----")
def getBiggerThan20(i):
    return i>20

lst = [10,25,30]
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)


print("----LAMBDA 함수----")
itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)
