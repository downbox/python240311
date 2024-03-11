# List 예제
my_list = [1, 2, 3, 4, 5] # 생성
print("List:", my_list)
my_list.append(6) # 요소 추가
print("List after append:", my_list)
my_list[1] = 10 # 요소 수정
print("List after modification:", my_list)

# Tuple 예제
my_tuple = (1, 2, 3, 4, 5) # 생성
print("\nTuple:", my_tuple)
# my_tuple[1] = 10 # 이 코드는 실행 시 오류를 발생시킴, 튜플은 수정할 수 없음

# Dictionary 예제
my_dict = {'a': 1, 'b': 2, 'c': 3} # 생성
print("\nDictionary:", my_dict)
my_dict['d'] = 4 # 새 키-값 쌍 추가
print("Dictionary after adding an element:", my_dict)
my_dict['a'] = 10 # 키 'a'의 값을 수정
print("Dictionary after modification:", my_dict)
