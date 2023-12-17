list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

for list in list_of_lists:
    all_higher_than_5 = True
    all_lower_than_5 = True
    for item in list:
        if item < 5:
            all_higher_than_5 = False
        elif item > 5:
            all_lower_than_5 = False

    print(list, all_lower_than_5, all_higher_than_5)

