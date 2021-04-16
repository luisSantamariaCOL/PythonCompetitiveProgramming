def main():
    list = ['H', 'Q', '9']
    word = input()
    word = [ch for ch in word]
    for ch in word:
        if ch in list:
            print("YES")
            return
    print("NO")

if __name__ == '__main__':
    main()