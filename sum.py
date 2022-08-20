def num(list1, list2):
    list = []
    lst = []
    i = len(list1) - 1
    j = len(list2) - 1
    k = 0
    while i >= 0 and j >= 0:
          list.append(list1[i] + list2[j])
          j -= 1
          i -= 1
          if len(str(list[k])) != len(str(list1[-1])):
             res = list[k] // 1000
             list[k] = list[k] % 1000
             lst.append(0)
             lst.append(res)
          else:
             lst.append(0)
             k +=1
    a = 0
    b = 0
    while a <= (len(lst) - 1) and b <= (len(list) - 1):
          list[b] += lst[a]
          a +=1
          b += 1      
    if len(str(list[-1])) > 3:
       list[-1] = list[-1] % 1000
       res1 = list[-1] // 100
       list.append(res1)
    list = list[::-1] 
    return list
list1 = [734,210,924]
list2 = [422,560,921]
print(num(list1, list2))

'''Lists lengths must be the same. If you want to give a smaller value than in the other list, write 0 (for example list1 = [0,0,123], list2 = [123,225,743]) 
