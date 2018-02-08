#!/usr/bin/env python
# -*-encoding:utf-8-*-


def merge_sort(List):
    mid = int(len(List) / 2)
    if len(List) <= 1: return List
    return merge(merge_sort(List[:mid]), merge_sort(List[mid:]))


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


def main():
    L = [1, 2, 3, 3, 6, 7, 10, 22, 11, 55, 33, 66]
    f = open('hw1test.txt')
    f.read()
    print(merge_sort(L))


if __name__ == "__main__":
    main()