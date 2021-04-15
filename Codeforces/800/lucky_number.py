def main():
    number = input()
    count_fours = 0
    count_seven = 0

    for digit in number:
        if digit == '4':
            count_fours+=1
        elif digit == '7':
            count_seven+=1

    total_count = count_fours+count_seven
    if total_count==4 or total_count==7:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()