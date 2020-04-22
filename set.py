"""
set: 无序不重复元素的序列
声明方式：1. 大括号{}
         2. set_param1 = set()
"""

# set_param = {"1","2","3"}
# print(set_param)
# print(type(set_param))
#
# print("1" in set_param)

# a = set("abcd")
# b = set("aqwe")
#
# print(a|b)
# print(a&b)

# 集合的CRUD
my_set = set(("to","ja","ro")) # 声明多个元素

my_set.add("ni")
my_set.remove("to")  # 移除指定元素
len(my_set)

print(my_set)
my_set.clear()   # 清除所有元素
print(my_set)











