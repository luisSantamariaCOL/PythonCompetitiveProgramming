def main():
    in_str = input()
    in_str = in_str.lower()
    vocals = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in range(len(vocals)):
        in_str = in_str.replace(vocals[i],'')

    out_str = ''
    for ch in in_str:
        out_str+='.'+ch

    return out_str


if __name__ == '__main__':
    print(main())