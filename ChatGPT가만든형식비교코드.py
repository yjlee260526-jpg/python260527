import time

# =====================================================================
# 1. 생성 및 기본 선언 (Syntax & Duplication)
# =====================================================================
print("--- 1. 기본 선언 및 중복 허용 여부 ---")

# List: 대괄호 [], 중복 허용, 순서 보존
my_list = [1, 2, 3, 3, 4]

# Tuple: 소괄호 (), 중복 허용, 순서 보존
my_tuple = (1, 2, 3, 3, 4)

# Set: 중괄호 {}, 중복 비허용, 순서 없음 (집합)
my_set = {1, 2, 3, 3, 4}

# Dict: 중괄호 {Key: Value}, Key 중복 비허용, Value 중복 허용
my_dict = {"apple": 1, "banana": 2, "cherry": 3, "cherry": 4} # Key 'cherry'가 중복되면 마지막 값으로 덮어써집니다.

print(f"List  : {my_list}")
print(f"Tuple : {my_tuple}")
print(f"Set   : {my_set}  <- 중복된 '3'이 자동으로 제거되었습니다.")
print(f"Dict  : {my_dict}  <- 중복된 Key 'cherry'의 값이 마지막 데이터(4)로 덮어씌워졌습니다.")
print()


# =====================================================================
# 2. 가변성 및 수정 가능 여부 (Mutability & Modification)
# =====================================================================
print("--- 2. 가변성 (Mutability) 테스트 ---")

# List: 요소를 자유롭게 변경, 추가, 삭제할 수 있습니다. (Mutable)
my_list[0] = 99
my_list.append(5)
print(f"Modified List : {my_list}")

# Tuple: 한 번 생성되면 요소를 수정할 수 없습니다. (Immutable)
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Tuple Modification Fail : {e} (Tuple은 내부 요소 수정이 불가능합니다.)")

# Set: 인덱스 수정은 불가능하지만(순서가 없기 때문), 요소를 추가/삭제할 수 있습니다. (Mutable)
my_set.add(5)
my_set.remove(1)
print(f"Modified Set  : {my_set}")

# Dict: Key를 사용해 Value를 자유롭게 수정하고 추가할 수 있습니다. (Mutable)
my_dict["apple"] = 100
my_dict["orange"] = 5
print(f"Modified Dict : {my_dict}")
print()


# =====================================================================
# 3. 요소 접근 방식 (Accessing Elements)
# =====================================================================
print("--- 3. 요소 접근 및 인덱싱 ---")

# List, Tuple: 인덱스(0부터 시작하는 숫자)로 접근
print(f"List index 1  : {my_list[1]}")
print(f"Tuple index 1 : {my_tuple[1]}")

# Dict: Key를 사용해 접근
print(f"Dict Key 'apple' value : {my_dict['apple']}")

# Set: 인덱싱을 지원하지 않으므로 개별 원소에 직접 접근하려면 반복문이나 형변환이 필요합니다.
print("Set : 인덱스로 직접 접근이 불가능하여, 주로 'in' 연산이나 반복문(for)을 사용합니다.")
print()


# =====================================================================
# 4. 탐색 속도 비교 (Performance: List vs Set)
# =====================================================================
print("--- 4. 탐색 속도 비교 (List vs Set) ---")
# 대량의 데이터를 준비합니다.
large_list = list(range(10_000_000))
large_set = set(large_list)
target = 9_999_999  # 탐색할 대상 (마지막 원소)

# List에서 원소 찾기 시간 측정
start_time = time.time()
is_in_list = target in large_list
list_time = time.time() - start_time

# Set에서 원소 찾기 시간 측정
start_time = time.time()
is_in_set = target in large_set
set_time = time.time() - start_time

print(f"List 탐색 시간 : {list_time:.6f} 초 (O(N) - 순차 탐색)")
print(f"Set 탐색 시간  : {set_time:.6f} 초 (O(1) - 해시 테이블 검색)")
print("Set은 내부적으로 해시 테이블을 사용하므로, 데이터의 크기와 무관하게 빠른 속도로 원소를 찾아낼 수 있습니다.")