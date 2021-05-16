#data structures
#hash
def main():
    n = int(input())
    users = {}
    for i in range(n):
        user = input()
        if user not in users:
            users[user] = 0
            print("OK")
        else:
            users[user] += 1
            new_username = user + str(users.get(user))
            print(new_username)


if __name__ == '__main__':
    main()