def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    print(" ".join(str(x) for x in num_list))

if __name__ == '__main__':
    main()