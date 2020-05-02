# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 01/05/2020 12.35

###########################
# 列表推导式    x for x in a

y = [x + 1 for x in [1, 2, 3, 4]]
# print(y)
# print(list(x +1 for x in [1, 2, 3, 4] if x > 2))
# print([x +1 for x in [1, 2, 3, 4] if x > 2])


# 快速排序
def qsort(my_list):
    if len(my_list) <= 1: return my_list
    return qsort([left_list for left_list in my_list[1:] if left_list < my_list[0]]) + \
           my_list[0:1] + \
           qsort([right_list for right_list in my_list[1:] if right_list >= my_list[0]])


def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        first  = my_list[0]
        left_list = quick_sort([l for l in my_list[1:] if l < first])
        right_list = quick_sort([l for l in my_list[1:] if l >= first])
        return  left_list + [first] + right_list


my_l = [3, 5, 1, 38 ,15, 8]
#print(qsort(my_l))
#print(quick_sort(my_l))


#########################
# 集合推导式

# y = [x + 1 for x in [1, 2, 3, 4]]
# print(y)
# print(type(y))
#
# y = {x + 1 for x in [1, 2, 3, 4]}
# print(y)
# print(type(y))


##########################
# 字典推导式

d = {x : y for x, y in {"a": 1, "b": 2}.items()}
print(d)


