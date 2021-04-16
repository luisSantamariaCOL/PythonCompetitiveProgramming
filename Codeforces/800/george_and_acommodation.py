def main():
    n = int(input())
    count = 0
    for i in range(n):
        people, capacity = input().split()
        people = int(people)
        capacity = int(capacity)
        if capacity-people >= 2:
            count+=1
    print(count)

if __name__ == '__main__':
    main()