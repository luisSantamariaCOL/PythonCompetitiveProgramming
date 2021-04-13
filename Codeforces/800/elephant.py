def main():
    coordinate_friendhouse = int(input())

    if coordinate_friendhouse < 5:
        return 1
    steps = int(coordinate_friendhouse/5)
    res = coordinate_friendhouse%5

    if res == 0:
        return steps
    else:
        return (steps+1)

if __name__ == '__main__':
    print(main())