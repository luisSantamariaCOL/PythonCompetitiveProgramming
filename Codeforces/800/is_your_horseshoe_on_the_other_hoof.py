def main():
    total_color = 4
    colors = list(map(int, input().split()))
    dict = {}
    for element in colors:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1

    # minimum number of horseshoes Valera needs to buy
    needs_to_buy = 4 - len(dict)
    print(needs_to_buy)

if __name__ == '__main__':
    main()

