# 정규표현식.py
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

# 연도 패턴
result = re.search("\d{4}", "올해는 2026년 입니다.")
print(result.group())

# 우편번호 패턴
result = re.search("\d{5}", "우리 동네는 52100 입니다.")
print(result.group())

# 특정 단어
result = re.search("apple", "This is an apple.".lower())
print(result.group())

