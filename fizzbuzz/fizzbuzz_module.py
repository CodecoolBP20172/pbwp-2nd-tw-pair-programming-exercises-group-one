def fizzbuzz(number):
    if number % 15 == 0:
        return("FizzBuzz")
    elif number % 3 == 0:
        return("Fizz")
    elif number % 5 == 0:
        return("Buzz")
    else:
        return number


def main():

    list = [i for i in range(101)]
    # print(list)

    for item in list:
        print(fizzbuzz(item))



if __name__ == '__main__':
    main()
