def main():
    n = int(input())
    elements = input()
    keys = []
    doors = []
    count = 0
    for e in elements:
        if e.islower():
            if e not in keys:
                keys.append(e)
        else:
            if e not in doors:
                doors.append(e)
            if e.lower() in keys:
                count+=1
                keys.pop(keys.index(e.lower()))

    print(count)

if __name__ == '__main__':
    main()