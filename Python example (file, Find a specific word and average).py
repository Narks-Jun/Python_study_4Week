# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s_num = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    find_colon = line.find(":")
    # print(find_colone)
    num = line[find_colon+2:]
    float_num = float(num)
    count = count + 1
    s_num = s_num + float_num
    # print(s_num)


print("Average spam confidence:", s_num / count )
