def main():
    array_1 =list(map(int, input().split()))
    array_2 =list(map(int, input().split()))
    # print(array_1)
    # print(array_2)
    if len(array_1) != len(array_2):
        print('Arrays must have equal sizes')
        return

    result_array = []
    for i in range(len(array_1)):
        result_array.append(array_1[i]+array_2[i])
    print(" ".join([str(x) for x in result_array]))



if __name__ == '__main__':
    main()