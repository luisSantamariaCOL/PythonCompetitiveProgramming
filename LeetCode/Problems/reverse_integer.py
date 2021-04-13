def reverse(number):
    str_num = str(number)
    if  len(str_num) == 1:
        return int(str_num)
    else:
        str_reversed = str_num[::-1]
        if  "0" in str_reversed:
            while True:
                if str_reversed.startswith("0"):
                    str_reversed = str_reversed[1:]
                else:
                    break

        if "-" in str_reversed:
            str_reversed = "-" + str_reversed[0:len(str_reversed)-1]
        return int(str_reversed)

def main():
    number = int(input())
    print(reverse(number))

if __name__ == "__main__":
    main()