'''
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

You have a positive integer m and a non-negative integer s.
Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s.
The required numbers should be non-negative integers written in the decimal base without leading zeroes.
'''

def lenght_and_sum_of_digits(n):
    n_string = str(n)
    list = [int(x) for x in n_string]
    return len(list), sum(list)

def main():
    dict = {}
    for i in range(901):
        if i not in dict:
            dict[i] = [[],[],[],[]]

    for i in range(1_000_000):
        m, s = lenght_and_sum_of_digits(i)
        dict[s][m-1].append(i)

    m, s = [int(x) for x in input().split()]
    try:
        print("{} {}".format(dict[s][m-1][0], dict[s][m-1][-1]))
    except:
        print("-1 -1")

if __name__ == '__main__':
    main()