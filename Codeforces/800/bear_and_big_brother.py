def main():
    limak, bob = input().split()
    limak = int(limak)
    bob = int(bob)
    n = bob

    if limak == bob:
        return 1

    i = 0
    while(True):
        if limak > bob:
            return i
        limak *= 3
        bob *= 2
        i+=1
    return -1

if __name__ == '__main__':
    print(main())