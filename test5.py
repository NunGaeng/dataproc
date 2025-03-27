a = range(10)
print(a)

add = 0
for j in range(1,11):
    add = add + j
    print(j, add)

print(add)

for j in range(2,10):
    for k in range(1,10):
        if j % 2 == 1 :
            print(j, ' * ', k, ' = ', j * k)
        #print(j * k, end=", ")
    print()

A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total = total + score
average = total / 10
print(average)

# diamond 그리기
diamond = int(input("숫자를 입력하세요 : "))
for j in range(diamond):
    space = abs(j - (diamond // 2))
    star = diamond - 2 * space
    #print(j, space, star)
    print(' ' * space + '*' * star)