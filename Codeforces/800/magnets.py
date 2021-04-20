def main():
    _list = [input() for _ in range(int(input()))]
    print(len([i for i in range(len(_list) - 1) if _list[i] != _list[i + 1]]) + 1)


if __name__ == '__main__':
    main()