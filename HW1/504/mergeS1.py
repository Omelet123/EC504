import time
# merge 2 sorted list together
def merge(l1, l2):
    tmp = []
    x = 0   # pointer of l1
    y = 0   # pointer of l2
    while x < len(l1) and y < len(l2):
        if l1[x] < l2[y]:
            tmp.append(l1[x])
            x += 1
        else:
            tmp.append(l2[y])
            y += 1

    if x == len(l1):
        for i in l2[y:]:
            tmp.append(i)
    else:
        for i in l1[x:]:
            tmp.append(i)

    return tmp


# read data from file
f = open("/Users/gaocc/PycharmProjects/504/hw1test.txt")
lines = f.readlines()
list = []  # use to store the lists, 200 lists in total,
for item in lines:
    content = item.strip()
    temp = content.split(" ")
    list.append(temp)
f.close()

# change the data type to int
newlist = []
for i in range(1, 201):
    change = [int(i) for i in list[i]]
    newlist.append(change)
# print(newlist)

# we can change n here, each list contain n data
str = input("Set n here(1<= m<= 100): ")
n = int(str)
generateL = []
for i in range(0, 200):
    a = newlist[i]
    generate = a[0:n]
    generateL.append(generate)
print(generateL)


t1 = time.clock()
middle = 1
while middle < 200:
    for i in range(0, 200 - middle, middle*2):
        generateL[i] = merge(generateL[i], generateL[i+middle])
    middle = middle*2
t2 = time.clock()
print("time: ", t2-t1)
# print(len(newlist[0]))

