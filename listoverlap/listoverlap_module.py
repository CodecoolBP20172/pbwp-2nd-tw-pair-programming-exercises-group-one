def listoverlap(list1, list2):
    setlist = []
    setlist2 = []
    result = []
    for number in list1:
        if number not in setlist:
            setlist.append(number)
    for number in list2:
        if number not in setlist2:
            setlist2.append(number)

    for number in setlist:
        if number in setlist2:
            result.append(number)
    print(result)


def main():
    a = [1, 1, 2, 3, 5, 5, 8, 8, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    listoverlap(a, b)


if __name__ == '__main__':
    main()
