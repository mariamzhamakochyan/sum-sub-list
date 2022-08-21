def sub(list1, list2):
    list = []
    new_list2 = [-x for x in list2]
    i = len(list1) - 1
    j = len(new_list2) - 1
    while i >= 0 and j >= 0:
        list.append(list1[i] + new_list2[j])
        i -=1
        j -=1
    for n in range(0, len(list)):
        if list[n] < 0:
           list[n] *= (-1)
    for k in range(0, len(list)): 
          if len(str(list[k])) != 3:
             list[k] = str(list[k] % 1000)
          k += 1
    list = list[::-1]
    return list
list1 = [342,522,950]
list2 = [134,592,386]
print(sub(list1, list2))
