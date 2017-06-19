def palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")

    i = 0
    j = len(string)-1
    while True:
        if string[i] != string[j]:
            return False
        elif i > j:
            return True
        i += 1
        j -= 1


def main():
    print(palindrome("A nut for a jar of tuna"))


if __name__ == '__main__':
    main()
