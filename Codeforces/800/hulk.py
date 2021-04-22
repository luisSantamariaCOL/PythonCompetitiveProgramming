def main():
    n = int(input())
    if n == 1:
        print('I hate it')
        return

    hate = True
    result = ''
    for i in range(n):
        if hate:
            result += 'I hate that '
        else:
            result += 'I love that '
        hate = not hate
    result = result[:len(result)-5] + 'it'
    print(result)

if __name__ == '__main__':
    main()