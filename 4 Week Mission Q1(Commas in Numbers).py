# f"{숫자:,}"
# print(f"{1000:,}"

def userInput() :
    while True :
        try :
            num = float(input("Input Number:"))
            break
        except :
            print("Invaild input. Please enter numeric input.")
    return num

def comma_num(a) :
    # 역순으로 뒤집어 정렬하기
    reversed_a = [i for i in reversed(a)]
    # print(reversed_a)
    # print(len(reversed_a))

    # 4번째 숫자마다 앞에 ,붙이기
    n = 3
    while n < len(reversed_a) :
        reversed_a[n] = "," + reversed_a[n]
        n = n + 3
    # print(reversed_a)

    # list > str로 변환
    # b = "".join(reversed_a) 로 사용 가능
    b = ""
    for i in reversed_a :
        b = b + i
    # print(b)

    # str > list로 변환하면서 역순으로 뒤집기
    reversed_reversed_a = [i for i in reversed(b)]
    # print(reversed_reversed_a)

    # list > str로 변환
    # c = "".join(reversed_reversed_a) 로 사용 가능
    c = ""
    for i in reversed_reversed_a :
        c = c + i
    # print(c)
    # print(type(c))
    return c

# 정수인지 소수인지 확인
def int_or_float(x) :
    if int(x) == float(x):
        x = int(x)
        x = str(x)
        return comma_num(x)
    else:
        x = str(x)
        k = x.find(".")
        x_integer = x[:k]
        x_decimal_notation = x[k + 1:]
        # print(x_integer)
        # print(x_decimal_notation)
        return comma_num(x_integer) + "." + x_decimal_notation

# 음수인지 아닌지 확인
def check_nagative(y) :
    if float(y) < 0 :
        y = abs(y)
        print(f"-{int_or_float(y)}")
        # type(int_or_float(y))

    else :
        print(int_or_float(y))

u = userInput()
check_nagative(u)
# comma_num(userInput())
