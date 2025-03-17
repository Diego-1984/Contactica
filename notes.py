my_list = [1, 2, 3,-2, 5, -3]

def max_sum(my_list):
    my_list_copy = my_list[:]
    my_list_copy2 = my_list[::-1]
    new_list = [sum(my_list)]
    new_list2 = [sum(my_list)]   
    
    for _ in range(len(my_list)-1):
        my_list_copy.pop(-1)
        new_list.append(sum(my_list_copy))
    
    for _ in range(len(my_list)-1):
        my_list_copy2.pop(-1)
        new_list2.append(sum(my_list_copy2))
    
    max1 = max(new_list)
    max2 = max(new_list2)
       
    if max1 >= max2:
        max_index = new_list.index(max1)
        return [max1, my_list[:len(my_list)-max_index]]
    else:
        max_index2 = new_list2.index(max2)
        return [max2, my_list[len(my_list)-max_index2-1:]][::-1]

my_list = [1, 2, 3, -2, 5, -3]
print(max_sum(my_list))



        
