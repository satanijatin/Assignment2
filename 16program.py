def is_sublist(main_list, sublist):
 
    for i in range(len(main_list)):
      
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [4, 5, 6,10]

if is_sublist(main_list, sub_list):
    print("The list contains the sub-list.")
else:
    print("The list does not contain the sub-list.")
