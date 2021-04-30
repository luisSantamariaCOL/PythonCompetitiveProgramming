def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    evens = [x for x in range(101) if x % 2 == 0]
    odds = [x for x in range(100) if x % 2 == 1]

    if len(set(numbers)) == 2:
        unique = [x for x in numbers if numbers.count(x) == 1]
        i = numbers.index(unique[0])
        print(i + 1)
        return

    evens_in_list = []
    odds_in_list = []
    for i in range(n):
        if numbers[i] in evens:
            evens_in_list.append(numbers[i])
        else:
            odds_in_list.append(numbers[i])
    if len(evens_in_list) == 1:
        i = numbers.index(evens_in_list[0])
        print(i+1)
    elif len(odds_in_list) == 1:
        i = numbers.index(odds_in_list[0])
        print(i + 1)


if __name__ == '__main__':
    main()