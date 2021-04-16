def main():
    lucky = [4,7,47,74,44,77,444,447,474,744,777,774,747,477]
    number = int(input())
    for i in range(len(lucky)):
        if number%lucky[i]==0:
            print("YES")
            return
    print("NO")


if __name__ == '__main__':
    main()