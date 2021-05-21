def main():
    n = int(input())
    elements = input()
    keys = []
    doors = []
    count = 0
    print(keys)
    for e in elements:
        if e.islower():
            if e not in keys:
                keys.append(e)
        else:
            if e not in doors:
                doors.append(e)
            if e.lower() in keys:
                keys.pop(keys.index(e.lower()))
            else:
                count += 1

    print(count)

if __name__ == '__main__':
    main()