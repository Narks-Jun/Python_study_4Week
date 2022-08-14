# copy text
# 특정 파일에서 특정 단어가 포함된 횟수에 대해서 작성된 코드입니다.
# split()을 통한 list 생성을 알아야 합니다.
# .count method 를 알면 더욱 쉽게 작성 가능합니다.

def save_txt(x):
    fh = open(x, "w", encoding='UTF8')
    # 클립보드는 시스템 영역이라 os 의 api 를 핸들링 해야 합니다. 그리고 os에 종속적입니다.
    # ctrl c, v 를 하려면 모듈을 설치해야 합니다
    import pyperclip
    clip_text = pyperclip.paste()
    # print(clip_text)
    fh.write(clip_text.replace("\n",""))
    fh.close()


def count_text(y, z) :
    fh = open(y, "r", encoding='UTF8')
    read_text = fh.read()

    # print(read_text.count("def")) 아래보다 훨씬 간단함.
    count = 0
    for w in read_text.split() :
        if z in w :
            count = count + 1
    return count
    fh.close()

def file_name():
    try :
        file = input("Save as:")
        return file
    except :
        print("Plase input file name")
        quit()
a = file_name()
b = input("Enter the word you want to find:")

save_txt(a)
print(count_text(a, b))
