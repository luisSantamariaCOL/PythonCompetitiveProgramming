'''
Problem 429B - Codeforces - Vanya and Lanterns
by luisSantamariaCOL

Problem tags
binary search, implementation, math, sortings, *1200
'''

def main():
    # input
    n, l = [int(x) for x in input().split()]
    lanterns = list(map(int, input().split()))
    lanterns = sorted(lanterns) # O(n log n)

    max_radius = 0
    for i in range(n):
        if i == 0:
            max_radius = lanterns[i]
            continue
        radius = lanterns[i] - lanterns[i-1]
        radius /= 2
        if radius > max_radius:
            max_radius = radius

    radius = l - lanterns[-1]
    if radius > max_radius:
        max_radius = radius
    print(max_radius)


if __name__ == '__main__':
    main()