def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    total = n*100
    print(sum(num_list)*100/total)

if __name__ == '__main__':
    main()