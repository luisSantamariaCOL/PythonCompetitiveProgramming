'''
    The problem is to find if a number is a T prime.
    A number is called a T prime if it has only 3 divisors.
    Solution:
    =========
    A number is a T prime if it is a perfect square
    and its square root is a prime number.
    4 is the only even number which is a T prime number.
'''

limit = 1000000
def calculate_prime_for_each_number_upto_limit():
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False
    for i in range(2, limit):
        if prime_flag[i]:
            for j in range(i*i, limit, i):
                prime_flag[j] = False
    return prime_flag

def check_if_number_is_tprime(n):
    global prime_flag
    if n==4:
        return True
    if n < 4 or n%2==0:
        return False
    sqrt_n = n**0.5
    if sqrt_n==int(sqrt_n):
        if prime_flag[int(sqrt_n)]:
            return True
    return False

prime_flag = calculate_prime_for_each_number_upto_limit()
def main():
    total_numbers = int(input())
    input_array = list(map(int, input().split()))
    for i in input_array:
        if check_if_number_is_tprime(i)==True:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()