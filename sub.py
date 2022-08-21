def sub(list1, list2):
    list = []
    new_list2 = [-x for x in list2]
    i = len(list1) - 1
    j = len(new_list2) - 1
    while i >= 0 and j >= 0:
        list.append(str(list1[i]) + str(new_list2[j]))
        i -=1
        j -=1
    list = list[::-1]
    return str(list)
list1 = [342,522,950]
list2 = [134,592,386]
print(sub(list1, list2))
