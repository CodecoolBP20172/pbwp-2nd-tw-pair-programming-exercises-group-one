import datetime


def years(age=0):
    year = ""
    date = (str(datetime.date.today()))
    for i in range(4):
        year += date[i]
    year = int(year)

    print(year - age + 100)


def main():
    years(24)


if __name__ == '__main__':
    main()
