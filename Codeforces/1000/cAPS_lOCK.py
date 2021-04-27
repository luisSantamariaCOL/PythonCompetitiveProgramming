def main():
    word = input()

    # 1 len cases
    if len(word) == 1:
        if word.isupper():
            print(word.lower())
        else:
            print(word.upper())
    else:
        # cap case
        if word.isupper():
            print(word.lower())
        elif word[0].islower() and word[1:].isupper():
            print(word.capitalize())
        else:
            print(word)


if __name__ == '__main__':
    main()