def main():
    n = input()
    numbers = [int(x) for x in input().split()]

    is_evens = [x % 2 for x in numbers]

    if is_evens.count(0) > is_evens.count(1):
        print(is_evens.index(1) + 1)
    else:
        print(is_evens.index(0) + 1)

if __name__ == '__main__':
    main()