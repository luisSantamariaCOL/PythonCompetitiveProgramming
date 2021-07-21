num_list = [3,8,10,9,32,7,15,4]
print(num_list)

# num_list[1], num_list[-1] = num_list[-1], num_list[1]

print("What numbers do you want to change?")

index_first_number = index_second_number = -1

while index_first_number  == -1 or index_second_number == -1:
    number_one = int(input("First number: "))
    number_two = int(input("Two number: "))

    try: index_first_number = num_list.index(number_one)
    except:
        index_first_number = -1
        print("Wrong first number")

    try: index_second_number = num_list.index(number_two)
    except:
        index_second_number = -1
        print("Wrong second number")

    if index_first_number != -1 and index_second_number != -1:
        num_list[index_first_number], num_list[index_second_number] = num_list[index_second_number], num_list[index_first_number]

print(num_list)