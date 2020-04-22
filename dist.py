"""
字典是一种可变容器模型，可以储存任意类型对象
"""
d = {1:"zhang3", 2:"li4"}    # 一对一对的 key:value
print(d)

keys = d.keys()    # 获取所有的key
#keys = d.get()     # 访问
print(keys)

for i in keys:
    print(i)
    print(d[i])

# 添加
# d[3]= "test"
# print(d)
# d.setdefault(4,"aaa")
# print(d)

# 更新
d[4] = "bbb"
print(d)

# delete
# r = d.pop(4)  # 删除并返回被删值
# print(r)
# print(d)
del d[4]
print(d)
