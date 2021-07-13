'''
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

You have a positive integer m and a non-negative integer s.
Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s.
The required numbers should be non-negative integers written in the decimal base without leading zeroes.
'''

def main():
    m, s = [int(x) for x in input().split()]

    if s == 0:
        print("0 0" if m == 1 else "-1 -1")
        return

    sum_of_digits = s
    min, max = '', ''

    for i in range(m):
        if s >= 9:
            max += '9'
            s -= 9
        else:
            max += str(s)
            s = 0

    min = [int(x) for x in reversed(max)]
    flag = False
    for i, digit in enumerate(min):
        if i == 0 and digit == 0:
            min[i] += 1
            flag = True
        elif digit > 0 and flag:
            min[i] -= 1
            flag = False

    if sum(min) == sum_of_digits:
        min = "".join([str(x) for x in min])
        print(min, max)
    else:
        print("-1 -1")

if __name__ == '__main__':
    main()
