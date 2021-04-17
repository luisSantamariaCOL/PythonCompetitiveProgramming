def main():
    n = int(input())
    l = input().split()
    l = [int(x) for x in l]
    result = [0]*n

    for i in range(n):
        result[l[i]-1] = i+1

    print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()