'''
Space Traveling Problem
by luisSantamariaCOL

paths:
["Mars Saturn"]
["Sun Earth", "Mercury Venus", "Mars Mercury", "Mercury Saturn"]

posible paths:
Mars Saturn
Mars Mercury Venus
Mars Mercury Saturn
Sun Earth

Expected output:
Mars Mercury Venus
Sun Earth
'''

def main():
    paths = {}
    n = int(input())
    for i in range(n):
        first_p, second_p = input().split()
        if first_p not in paths:
            paths[first_p] = [second_p]
        else:
            paths.get(first_p).append(second_p)

    print(paths)

if __name__ == '__main__':
    main()
