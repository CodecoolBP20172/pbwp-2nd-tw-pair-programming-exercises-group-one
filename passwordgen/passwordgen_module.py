import random
import sys


def passwordgen():
    for i in range(8):
        sys.stdout.write(chr(random.randint(33, 127)))


def main():
    passwordgen()


if __name__ == '__main__':
    main()
