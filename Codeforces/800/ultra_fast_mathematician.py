def main():
    s1 = input()
    s2 = input()

    output = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            output += '0'
        else:
            output += '1'
    print(output)

if __name__ == '__main__':
    main()