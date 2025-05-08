## 문자열
# 문자열 길이 구하기
a = "Life is too short"
print(len(a))      # 문자열 길이를 구하는 함수 len

# 문자열 인덱싱
a = "Life is too short, You need python"
print(a[3])
print(a[-1])        # 거꾸로도 가능

# 문자열 슬라이싱
a = "Life is too short, You need python"
print(a[0:4])       # 단 끝자리는 포함하지 않음
print(a[19:])       # 끝번호를 지정하지 않으면 모두 출력
print(a[:17])       # 시작번호를 지정하지 않으면 끝번호까지 출력
print(a[:])         # 처음부터 끝까지
print(a[19:-7])     # 19번째부터 뒤에서 8번째까지


## 리스트
# 리스트 안의 리스트
a = [1,2,3,['a','b','c']]
print(a[3])
print(a[3][1])

# 리스트 연산하기
a = [1,2,3]
b = [4,5,6]
print(a + b)        # 더하기
print(a * 3)        # 반복하기
print(len(a))       # 길이 구하기
#print(a[2] + "hi") # << 오류 걸림
print(str(a[2]) + "hi") # string으로 변환 해줘야 함 (시험 x)

# 리스트 요소 추가
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

# index 반환
a = [1,2,3]
print(a.index(3))       # index(x) 리스트에 x값이 있으면 위치를 알려줌

# 리스트 요소 끄집어내기 (pop) (시험 x)
a = [1,2,3]
a.pop()     # 맨 마지막 요소를 리턴하고 그 요소는 삭제
print(a)

a = [1,2,3]
a.pop(1)    # 리스트의 x번째 요소를 리턴하고 그 요소는 삭제
print(a)

# 리스트의 x 개수 세기
a = [1,2,3,1]
print(a.count(1))


## 튜플
# 튜플은 수정이 불가능
a = (1,2,3)
# a.append(5)       # << error
print(a)


## 딕셔너리
a = {1,2,3}
print(a)


## 불(bool) 자료형
# 참과 거짓을 나타내는 자료형
print(bool('python'))


## 문제
# 문제 1
triangle = 7
center = triangle // 2

for j in range(-center, center+1):
    #num_star = abs((abs(j) + (abs(j)+1)) - 8)
    num_star = triangle - 2 * abs(j)
    to_print = '*' * num_star
    print(to_print)

# 문제 2
data = [1,2,3,4,2,1,3,1,2,2]

count_data = []
for j in data:
    count_data.append(data.count(j))
max_freq = max(count_data)
max_num = data[count_data.index(max_freq)]

print(f'최빈치 : {max_num}, 개수 : {max_freq}')

# 문제 변형 1
height = 5
center = height // 2
for j in range(-center, center+1):
    star = height - 2 * abs(j)
    blank = abs(j)
    print(f'{blank * ' '}{star * '*'}')

# 문제 변형 2
data = [4, 5, 6, 5, 4, 3, 2, 1, 4, 5, 6, 6]

count_data = []
for j in data:
    count_data.append(data.count(j))

