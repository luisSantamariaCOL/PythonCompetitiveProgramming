def main():
    n = int(input())
    num_list = []

    num_list = input().split()
    num_list = [int(x) for x in num_list]
    num_list.sort(reverse=True)
    num_sum = sum(num_list)
    x = 0
    i = 0
    while x <= num_sum/2:
        x += num_list[i]
        i += 1
    print(i)

if __name__ == '__main__':
    main()