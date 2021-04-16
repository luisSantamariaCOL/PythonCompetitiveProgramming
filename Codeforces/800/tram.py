def main():
    n = int(input())
    passenger_count = 0
    max = 0
    for i in range(n):
        exit, enter = input().split()
        exit = int(exit)
        enter = int(enter)
        passenger_count -= exit
        passenger_count += enter
        if  passenger_count > max:
            max = passenger_count
    print(max)

if __name__ == '__main__':
    main()