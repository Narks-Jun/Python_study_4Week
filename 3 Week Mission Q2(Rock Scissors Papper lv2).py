

user = "가위 바위 보 게임에 오신걸 환영합니다."
print(user)
rsp = ["가위", "바위", "보"]

# 가위 바위 보 게임을 몇 번 할 지 입력
def how_many_games() :
    while True:
        try :
            h = int(input("몇 판을 진행하시겠습니까?:"))
            if h >= 1 :
                break
            else :
                print("0보다 커야합니다.")
        except :
            print("횟 수를 입력해주세요.")
    return h

# 가위 바위 보의 입력 값을 정수 형태로 변환
def getUserInput():
    while True : # while을 통해 입력값이 제대로 될때까지 반복
        a = input("가위 바위 보:")
        if a not in rsp :
            print("가위 바위 보를 입력하세요.")
            continue
        if a == rsp[0] :
            user = int(0)
        elif a == rsp[1] :
            user = int(1)
        elif a == rsp[2] :
            user = int(2)
        break
    return user

# 연산을 이용한 결과출력 방법
def game(u, c) :
    result = u - c
    # print(result)
    if result == 0 :
       result = "비겼습니다!"
    elif result == -1 or result == 2 :
        result = "컴퓨터 승리!"
    elif result == 1 or result == -2 :
        result = "유저 승리!"
    else :
        print("Error1")
    return result

# 정수 값을 가위 바위 보로 변환
def getResult (b) :
    r = "결과"
    if b == 0:
        r = rsp[0]
    elif b == 1:
        r = rsp[1]
    elif b == 2:
        r = rsp[2]
    else:
        print("Error2")
    return r

# 승패 결과를 counting - 매개 변수를 함수내에서 업데이트 해주어야 하기때문에 굳이 함수로 작성하지 않아도 된다.
def wdd(x, y, z) :
    if gr == "비겼습니다!":
        x = x + 1
    elif gr == "컴퓨터 승리!":
        y = y + 1
    elif gr == "유저 승리!":
        z = z + 1
    return x, y, z

# 최종 결과
def total(x, y, z) :
    print("유저의 전적:", x,"승", y,"무", z,"패")
    print("컴퓨터의 전적:", z,"승", y,"무", x,"패")
    return x, y, z


t = 1
times = how_many_games()
draw = 0
win_com = 0
win_user = 0

while t <= times :
    u = getUserInput()
    # print(u)

    import random
    computer = random.randint(0, 2)
    c = int(computer)
    # print(c)

    gr = game(u, c)

    # ----------------------------------------
    if gr == "비겼습니다!" :
        draw = draw + 1
    elif gr == "컴퓨터 승리!" :
        win_com = win_com + 1
    elif gr == "유저 승리!" :
        win_user = win_user + 1
    # ----------------------------------------
    # wdd(draw, win_com, win_user) 해당부분을 함수로 변경하려면면 함수에 값을 다시 업데이트 하는 과정이 필요
    # draw, win_com, win_user = wdd(draw, win_com, win_user)
    # https://pythonguides.com/python-pass-by-reference-or-value/

    print("유저 =", getResult(u))
    print("컴퓨터 =", getResult(c))
    print(t,"번째 판", gr)

    t = t + 1

total(win_user, draw, win_com)
