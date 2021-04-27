def main():
    n = int(input())
    seq = list(map(int, input().split()))

    max = 0
    count = 0
    for i in range(len(seq)):
        if i == 0:
            count += 1
            max = count
            continue
        if seq[i] >= seq[i-1]:
            count += 1
            if count > max:
                max = count
        else:
            count = 1
    print(max)

if __name__ == '__main__':
    main()