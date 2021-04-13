import math

# What is the least number of flagstones needed to pave an n*m Square?
# flagstones have a size of a*a
def main():
    n, m, a = input().split()
    n = int(n)
    m = int(m)
    a = int(a)

    return math.ceil(n/a) * math.ceil(m/a)

if __name__ == '__main__':
    print(main())

# Input
# 6 6 4

# Output
# 4