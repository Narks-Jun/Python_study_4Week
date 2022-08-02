

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

numbers = [i for i in range(n,m+1)]
# print(numbers)
natural_number = [w for w in range(2, m+1)]
# print(natural_number)
o = [] # 함수결과를 리스트에 추가하기 위해 전역변수 선언

# x가 소수라면 True 값을 반환하는 함수
def tf(x) :
    for y in natural_number:
        if x <= 1 :  # 1은 소수가 아님
            return False
        elif x > y:  # 나눗셈 결과가 정수라면 소수가 아님
            z = x / y
            if z == int(z):
                return False
        else:
            return True

# 소수의 갯수를 세는 함수
def count_prime_number() :
    count = 0
    for k in numbers :
        tf(k)
        if tf(k) == True :
            # print(K)
            count = count + 1
            o.append(k) # k값을 o안에 추가함
        else :
            pass
    # print(count)
    return count
    # return o 함수 실행 후 결과값을 리스트로 만들려면 o를 반환

count_nunmer = count_prime_number()
print("소수개수", count_nunmer)

# 소수 값을 구해 리스트로 만든 후 항목의 갯수를 센다면
def count_olist() :
    count_o = 0
    for q in o :
        count_o = count_o + 1
    return count_o
# print("소수개수", count_olist())
# 더간단하게 가능
# print(len(o))
