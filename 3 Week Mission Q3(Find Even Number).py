

while True :
    try :
        n = int(input("첫 번째 숫자를 입력하세요:"))
        break
    except :
        print("정수를 입력하세요")
        continue

while True :
    try :
        m = int(input("마지막 숫자를 입력하세요:"))
        if m > n :
            break
        if m <= n :
            print("첫 번쨰 숫자보다 커야합니다.")
    except :
        print("정수를 입력하세요")
        continue

# range(시작 숫자, 끝 숫자 + 1)
numbers = [i for i in range(n,m+1)]
middle_number = (n+m)/2
# print(numbers)
# print(middle_number)
# print(int(middle_number))

def result(n, m) :
    for x in numbers :
        if x/2 == int(x/2) : # 짝수인지 확인
            print(x, "짝수")
            if x == middle_number : # 중앙값인지 확인
                print(x, "중앙값")

result(n, m)

