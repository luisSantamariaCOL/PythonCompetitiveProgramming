def main():
    players = input()
    if "1"*7 in players or "0"*7 in players:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
