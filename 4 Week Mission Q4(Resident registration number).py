
def userinput_with_hyphen():
    while True:
        try :
            id = input("Please enter your ID number:")
            if not "-" in id:
                print("Please enter ID Number with hyphen")
                continue
            elif len(id) != 14 :
                print("ID number must be 14 digits")
                continue
            elif not id.find("-") == 6 :
                print("Enter year and month without century")
                continue
            int(id[:6])
            int(id[7:])
            if not int(id[2:4]) < 13 :
                print("Please enter a number under 13 for the month")
                continue
            if not int(id[4:6]) < 32:
                print("Please enter a number under 32 for the date")
                continue
            return id
        except :
            print("Please enter the numeric input")
            continue

# 하이픈 없는게 예외 케이스가 더 적다(?)
def userinput_without_hyphen():
    while True:
        try :
            id = input("Please enter your ID number:")
            int_id = int(id)
            if len(id) != 13 :
                print("ID number must be 13 digits")
                continue
            if not int(id[2:4]) < 13 :
                print("Please enter a number under 13 for the month")
                continue
            if not int(id[4:6]) < 32:
                print("Please enter a number under 32 for the date")
                continue
            return id
        except :
            if "-" in id :
                print("Please enter ID Number without hyphen")
                continue
            else :
                print("Please enter the numeric input")
                continue

def id_number(x):
    front = x[:6]
    birth_year = front[:2]
    birth_month = front[2:4]
    back = x[7:]
    gender = back[:1]
    # print(gender)
    ig = int(gender)
    if 22 >= int(birth_year) >= 00 :
        while True:
            check_year = input("2000년생 이후 출생자 입니까? 맞으면 o 아니면 x:")
            if check_year == "o":
                if ig == 3 or ig == 7 :
                    return birth_year, birth_month, True  # True는 남자 출력 예정
                elif ig == 4 or ig == 8 :
                    return birth_year, birth_month, False  # False는 여자 출력 예정
                else:
                    print("잘못된 번호 입니다\n올바른 번호를 넣어 주세요")
                    quit()
            elif check_year == "x":
                if ig == 1 or ig == 5 :
                    return birth_year, birth_month, True
                elif ig == 2 or ig == 6 :
                    return birth_year, birth_month, False
                else :
                    print("살아있는 사람이 아닙니다")
                    quit()
            else:
                print("Please enter o or x")
                continue
    else :
        if ig == 1 or ig == 3 :
            return birth_year, birth_month, True
        elif ig == 2 or ig == 4 :
            return birth_year, birth_month, False

def man_or_woman(x, y, z):
    if z is True :
        print(f"{x}년{y}월 남자")
    else :
        print(f"{x}년{y}월 여자")


a = userinput_with_hyphen()
birth_year, birth_month, True_or_False = id_number(a)
man_or_woman(birth_year, birth_month, True_or_False)
