def main():
    n = int(input())
    x = [y for y in input().split()]
    if '1' in x: print("HARD")
    else: print("EASY")


if __name__ == '__main__':
    main()