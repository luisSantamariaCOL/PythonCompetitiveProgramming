def main():
    s = input()
    a = s.find('AB')
    b = s.find('BA', a+2)
    c = s.find('BA')
    d = s.find('AB', c+2)
    if (a!=-1 and b!=-1 or c!=-1 and d!=-1): print("YES")
    else: print("NO")


if __name__ == '__main__':
    main()