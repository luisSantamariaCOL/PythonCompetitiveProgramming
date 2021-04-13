def main():
    number, subtraction = input().split()
    number = int(number)
    subtraction = int(subtraction)

    for i in range(subtraction):
        if number%10 == 0:
            number/=10
        else:
            number-=1
    print(round(number))


if __name__ == '__main__':
    main()