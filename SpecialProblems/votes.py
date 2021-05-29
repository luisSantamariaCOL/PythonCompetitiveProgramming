# seventyfice -> 25
# fourtythree -> 43
# twenty -> 20
# nine -> 9
# thirtythree -> 22

def vote_validation(str_vote : str):
    if str_vote.isalpha():
        return 1
    else:
        return 0


def convert_vote(str_vote):
    if not vote_validation(str_vote):
        return 0
    return 1

def voting(total_count):
    vote = input("Enter vote: ")
    count = convert_vote(vote)
    total_count += count

if __name__ == '__main__':
    conversion = {'one': 1,
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
        voting(total_count)
        print("Enter '0' or 'exit' to exit")
        choice = input()
        if choice == '0' or choice.lower() == 'exit':
            break
