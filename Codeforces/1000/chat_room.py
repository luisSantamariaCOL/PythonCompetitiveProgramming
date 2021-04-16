def main(s):
    hello_in_list = [ch for ch in 'hello']
    s_in_list = [ch for ch in s]
    h_count = 0
    for i in range(len(s_in_list)):
        if h_count==0:
            if s_in_list[i] == hello_in_list[h_count]:
                h_count +=1
                if h_count==5:
                    break
            else:
                continue
        if h_count > 0:
            if s_in_list[i] == hello_in_list[h_count]:
                h_count +=1
                if h_count==5:
                    break
            elif s_in_list[i] == hello_in_list[h_count-1]:
                continue
            else:
                h_count==0

    if h_count == 5:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    s = input()
    main(s)