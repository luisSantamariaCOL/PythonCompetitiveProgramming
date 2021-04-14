def main():
    word = input()
    lower_count = 0
    upper_count = 0

    for ch in word:
        if ch.islower():
            lower_count+=1
        else:
            upper_count+=1

    if upper_count > lower_count:
        return word.upper()
    else:
        return word.lower()


if __name__ == '__main__':
    print(main())