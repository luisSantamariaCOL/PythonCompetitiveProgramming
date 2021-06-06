def main():
    n, m, a, b = list(map(int ,input().split()))
    minimum_money_to_spend = 0
    if a*m < b:
        minimum_money_to_spend = a*n
    else:
        minimum_money_to_spend = (n//m)*b + (n%m)*a
    print(minimum_money_to_spend)

if __name__ == '__main__':
    main()