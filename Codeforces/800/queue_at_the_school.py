def main():
    n,t = input().split()
    n = int(n)
    t = int(t)
    queue = list(input())
    while(t>0):
        i = 0
        while i < len(queue):
            if i < len(queue)-1:
                if queue[i]=='B' and queue[i+1]=='G':
                    queue[i] = 'G'
                    queue[i+1] = 'B'
                    i+=1
            i+=1
        t-=1
    print("".join(queue))

if __name__ == '__main__':
    main()