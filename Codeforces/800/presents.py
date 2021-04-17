def main():
    n = int(input())
    gift_list = input().split()
    gift_list = [int(x) for x in gift_list]
    result = [0]*n

    for i in range(n):
        result[gift_list[i]-1] = i+1

    print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()