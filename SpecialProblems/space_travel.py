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
def input_travels():
    paths = {}
    n = int(input())
    for i in range(n):
        first_p, second_p = input().split()
        if first_p not in paths:
            paths[first_p] = [second_p]
        else:
            paths.get(first_p).append(second_p)

    return paths

list_of_routes = []
def print_travels(paths):

    for first_p in paths:
        for destination in paths.get(first_p):
            print(first_p, destination)
    print(paths)
    print((len(paths)))


def main():
    paths = input_travels()
    print_travels(paths)


if __name__ == '__main__':
    main()
