def main():
    s1 = input()
    s2 = input()
    s_reverse = s1[::-1]

    if s_reverse == s2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()