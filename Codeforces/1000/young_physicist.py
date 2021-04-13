def main():
    x1, y1, z1 = [0,0,0]

    n = int(input())
    for i in range(n):
        x,y,z = input().split()
        x1 += int(x)
        y1 += int(y)
        z1 += int(z)

    if (x1==0 and y1==0 and z1==0):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(main())