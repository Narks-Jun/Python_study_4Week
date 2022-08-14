
def save_txt(x):
    fh = open(x, "w", encoding='UTF8')
    # 클립보드는 시스템 영역이라 os 의 api 를 핸들링 해야 합니다. 그리고 os에 종속적입니다.
    # ctrl c, v 를 하려면 모듈을 설치해야 합니다
    import pyperclip
    clip_text = pyperclip.paste()
    # print(clip_text)
    fh.write(clip_text.replace("\n",""))
    fh.close()

# 잘못 된 조건이 없을 경우 True 값으로 반환, 있을 경우 False 값으로 반환
def check_wrong_component(m, n):
    if not n.startswith("010"):
        return False
    elif not "-" in n:
        return False
    elif not len(n) == 13:
        return False
    else :
        return True

def find_wrong_guest(y):
    with open(y, "r", encoding='UTF8') as fh:
        x = fh.readlines()
        print("Guest_book")
        for i in x:
            i = i.strip()
            print(i)
        print("Wrong_guest_book")
        for i in x:
            # print(i)
            comma = i.find(",")
            guest_name = i[:comma]
            # print(guest_name)
            guest_number = i[comma + 1:]
            # print(guest_number)
            # print(len(guest_number))
            if check_wrong_component(guest_name, guest_number) is False:
                print(f"잘 못 쓴 사람:{guest_name}")
                print(f"잘 못 쓴 번호:{guest_number}")


a = "test1.txt"

save_txt(a)
find_wrong_guest(a)
