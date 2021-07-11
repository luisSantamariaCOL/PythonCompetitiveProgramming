'''
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

You have a positive integer m and a non-negative integer s.
Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s.
The required numbers should be non-negative integers written in the decimal base without leading zeroes.
'''


# def lenght_and_sum_of_digits(n):
#     n_string = str(n)
#     list = [int(x) for x in n_string]
#     return len(list), sum(list)


def main():
    m, s = [int(x) for x in input().split()]

    min, max = '', ''

    for i in range(m):
        if s >= 9:
            max += '9'
            s -= 9
        else:
            max += str(s)
            s = 0

    min = list(max)
    min.reverse()
    min = "".join(min)
    min = int(min)


    print(min, max)

    # try:
    #     print("{} {}".format(dict[s][m - 1][0], dict[s][m - 1][-1]))
    # except:
    #     print("-1 -1")

if __name__ == '__main__':
    main()
