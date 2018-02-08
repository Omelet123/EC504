import sys
f = open("/Users/gaocc/PycharmProjects/504/hw1test.txt")
lines = f.readlines()
list = []
for item in lines:
    # 清除换行、空格
    content = item.strip()
    # 按照","分割
    temp = content.split(",")
    list.append(temp)
f.close()
#print(list)
