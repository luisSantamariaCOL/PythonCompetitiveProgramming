def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    count1, count2, count3, count4 = 0,0,0,0

    for num in num_list:
        if num == 4: count4 +=1
        elif num == 3: count3 += 1
        elif num == 2: count2 += 1
        else: count1 += 1

    result = count4

    result += count2//2
    count2 = count2%2

    if count1 <= count3:
        result += count1
        result += count2
        result += count3 - count1
    else:
        result += count3
        count1 -= count3
        result += count1 // 4
        count1 %= 4

        res = count1 + count2 * 2
        if res > 0:
            result += 1 if res <= 4 else 2

    print(result)

if __name__ == '__main__':
    main()