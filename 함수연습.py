# 함수연습.py

def setValue(newValue):
    x = newValue
    print("함수내부:", x)

retValue = setValue(5)
print(retValue)

def swap(a,b):
    return b, a

retValue = swap(3,4)
print(retValue)


# 지역변수와 전역변수
x = 5
def func(a):
    return a+x

print(func(1))

def func2(a):
    x = 1
    return a+x

print(func2(1))


print("--기본값 명시--")
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "https://" + server + ':' + port
    return strURL

print(connectURI("multi.com","80"))
print(connectURI(port="8080", server="naver.com"))


print("--디버깅 예시--")

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result
        
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

print("--람다함수 예시--")

g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x)(3) )
print(dir())
print(globals)