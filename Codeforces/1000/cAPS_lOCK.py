def main():
    word = input()

    if len(word) == 1:
        if word.isupper():
            print(word.lower())
        else:
            print(word.upper())
    else:
        if word.isupper():
            print(word.lower())
        elif word[0].islower() and word[1:].isupper():
            print(word.capitalize())
        else:
            print(word)


if __name__ == '__main__':
    main()