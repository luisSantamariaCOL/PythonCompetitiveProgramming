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
                  'thirteen': 13,
                  'twenty':20,
                  'fifty':50,
                  'ty': 10,
                  'teen': 10,
                  'and':0,
                  'hundred':100,
                  'thousand':1_000,
                  'million':1_000_000}
    total_count = 0

    while True:
        vote = input("Enter vote: ")
        if not vote.isalpha():
            print("Not a valid vote")
        else:
            if vote in numbers:
                total_count += numbers[vote]
            else:
                current_vote = 0
                while len(vote) != 0:
                    for key in numbers:
                        if vote.startswith(key):
                            #print(key)
                            if key == 'teen':
                                current_vote += 10
                            elif key == 'ty':
                                current_vote *= 10
                            elif key == 'hundred':
                                current_vote *= 100
                            elif key == 'and':
                                current_vote += 0
                            elif key == 'thousand':
                                current_vote *= 1_000
                            elif key == 'million':
                                current_vote *= 1_000_000
                            else:
                                current_vote += numbers[key]
                            vote = vote[len(key)::]
                            #print(vote)
                total_count += current_vote
        print("Total count:", total_count)

if __name__ == '__main__':
    main()
