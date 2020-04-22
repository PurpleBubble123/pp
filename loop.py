

# list1 = [1,2,3]
# for l in list1:
#     print(l)
#
# i = 1
# while i<100:         #True:   # 条件要控制
#     i =  i+1
#     print(i)

# eg. sorted
a = [15, 3, 5, 1, 49, 52]

# a.sort()
# a.sort(reverse=True)   // 反向
#print(a)

# 冒泡循环
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]   # 两数交换







