def main():
    level = int(input())
    little_X = list(map(int, input().split()))
    little_Y = list(map(int, input().split()))

    d = []
    m = 0

    for i in range(1, little_X[0] + 1):
        d.append(little_X[i])
    for i in range(1, little_Y[0] + 1):
        d.append(little_Y[i])

    for i in range(1, level + 1):
        if (not (i in d)):
            m = 1
            print("Oh, my keyboard!")
            break

    if (m == 0):
        print("I become the guy.")

if __name__ == '__main__':
    main()