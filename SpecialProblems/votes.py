# seventyfice -> 25
# fourtythree -> 43
# twenty -> 20
# nine -> 9
# thirtythree -> 22

def main():
    numbers = {'one': 1,
                  'two': 2,
                  'three': 3,
                  'four': 4,
                  'five': 5,
                  'six': 6,
                  'seven': 7,
                  'eight': 8,
                  'nine': 9,
                  'ten': 10,
                  'eleven': 11,
                  'twelve': 12,
                  'teen': 10,
                  'twenty': 20,
                  'thirty': 30,
                  'fourty': 40,
                  'fivety': 50,
                  'sixty': 60,
                  'seventy': 70,
                  'eighty': 80,
                  'ninety': 90}
    total_count = 0

    while True:
        vote = input("Enter vote: ")
        if not vote.isalpha():
            print("Not a valid vote")
        else:
            if vote in numbers:
                total_count += numbers[vote]
        print("Total count:", total_count)

if __name__ == '__main__':
    main()
