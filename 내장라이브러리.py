# 내장라이브러리.py

import random

print(random.random())
print(random.random())
#구간을 지정
print(random.uniform(2.0, 5.0))
print(random.uniform(2.0, 5.0))
#리스트 랜덤하게 선택
items = ["apple","banana","cherry","date","elderberry"]
print(random.choice(items))
print(random.choice(items))

#루프를 돌면서 0에서 19까지의 숫자 중에서 랜덤하게 10개를 선택
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print("---샘플링---")
print(random.sample(range(20),10))
print(random.sample(range(20),10))
print(random.sample(range(20),10))

print("---로또번호---")
print(random.sample(range(1,46), 5))

print("---파일명 다루기---")
import os.path
fileName = "C:\\python313\\python.exe"
#raw string notation
fileName = r"C:\python313\python.exe"
print(os.path.basename(fileName))
print(os.path.abspath(fileName))

if os.path.exists(fileName):
    print("파일의 크기:{0}".format(os.path.getsize(fileName)))
else :
    print("파일이 존재하지 않습니다.")



print("---운영체제---")
import os
print("운영체제 이름:", os.name)
print("환경변수:", os.environ)
#os.system("notepad.exe")

print("---특정 폴더의 파일리스트---")
import glob
print(glob.glob("c:\\work\\*.*"))
print(glob.glob(r"c:\work\*.*"))

for item in glob.glob(r"c:\work\*.py"):
    print(item)