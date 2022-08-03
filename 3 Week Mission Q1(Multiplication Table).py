def multiplication_table() :
    while True:
        question = input("몇 단?:")
        try :
            x = int(question)
            if x >= 1 :
                if x > 50:
                    print("50이하의 자연수를 입력해주세요")
                else :
                    print(x, '단')
                    break
            else :
                print("자연수를 입력해주세요")
        except :
            print("숫자를 입력해주세요")
            continue

    y = 1

    while True :
        if x * y > 50 :
            break
        else :
            print(x, "X", y, "=", x*y)
            y = y + 2


multiplication_table()
