def max_number_in_list(a_list):
    max_number = 0
    for list in a_list:
        if list > max_number:
            max_number = list
        elif list < max_number:
            continue
    print("Max Number = " + str(max_number))

list_of_numbers = [12, 34, 23, 75, 43, 65]
max_number_in_list(list_of_numbers)
