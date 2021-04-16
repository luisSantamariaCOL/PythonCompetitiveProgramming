def main():
    nfriends, hfence = input().split()
    nfriends = int(nfriends)
    hfence = int(hfence)

    hfriends = input().split()
    hfriends = [int(x) for x in hfriends]

    sum = 0
    for h in hfriends:
        if h <= hfence:
            sum+=1
        else:
            sum+=2
    print(sum)

if __name__ == '__main__':
    main()