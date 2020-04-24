"""
循环的中断
1. break
2. continue   // 结束本轮循环，进入下一次循环
"""
i = 1
while True:
    i = i+1
    print(i)
    if i == 10:
        print("=10")
        continue
        print("this")
    print("next")
    if i ==15:
        break


