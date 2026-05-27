# DemoList.py

#리스트

lst = [1,2,3,4,5]
print(len(lst))

# 추가
lst.append(6)
print(lst)

# 삭제
lst.remove(3)
print(lst)

#슬라이싱
strA = 'python'
strB = '파이썬은 강력해'
strC = '''다중
라인은로
저장'''

print(strA)
print(strB[0])
print(strB[1])
print(strB[0:3])
print(strB[-3:])
print(strC)
print(len(strB))

#Set

a = {1,2,3,3}
b = {3,4,4,5}
print(a) 
print(b)
print(len(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple
tp = (10,20,30)
print(len(tp))
print(tp[0])
print(tp.index(30))

#여러개 리턴
def calc(a,b):
    return a+b, a*b

print(calc(3,4))
print("id:%s, name:%s" % ("kim","김유신"))

#형식 변환
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)