def main():
    n = int(input())
    if n%2==0:
        result = int(n/2)
    else:
        result = int(-(n+1)/2)
    print(result)

if __name__ == '__main__':
    main()