dict = {
    2:["a","b","c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}

def change_output_list(in_list, number):
    out_list = []
    list_to_add = dict.get(number)

    if  len(in_list) == 0:
        out_list = list_to_add
    else:
        for i in in_list:
            for j in list_to_add:
                out_list.append(i+j)
    return out_list

output_list = []
in_str = input()
list_of_numbers = [int(char) for char in in_str]


for i in list_of_numbers:
    in_list = output_list
    output_list = change_output_list(in_list, i)

print(output_list)


