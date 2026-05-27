# 파일연습.py

# 파일 객체 생성
f = open("test.txt", "wt", encoding="utf-8") 
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close()

# 파일 읽기
f = open("test.txt", "rt", encoding="utf-8")
content = f.read()
print(content)
f.close()

