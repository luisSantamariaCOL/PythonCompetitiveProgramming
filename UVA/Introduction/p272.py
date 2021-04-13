def main():
    first = True
    while True:
        try:
            mssg = str(input())
        except EOFError:
            break
        out = []
        for ch in mssg:
            if ch == '\"':
                if first:
                    out.append('``')
                else:
                    out.append('\'\'')
                first = not first
            else:
                out.append(ch)
        print("".join(out))
main()