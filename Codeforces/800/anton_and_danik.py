def main():
    number = input()
    s = input()
    D = s.count('D')
    A = s.count('A')

    if D > A:
        print("Danik")
    elif A > D:
        print("Anton")
    else:
        print("Friendship")

if __name__ == '__main__':
    main()