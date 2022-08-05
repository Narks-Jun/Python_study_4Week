sum_num = 0.0
count_num = 0

while True :
    input_num = input("Enter a number:")
    if input_num == "done":
        break
    try :
        float_num = float(input_num)
    except :
        print("Intput Numeric Number.")
        continue
    count_num = count_num + 1
    sum_num = sum_num + float_num

average = sum_num / count_num

print(sum_num, count_num, average)
