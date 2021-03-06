# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 02/05/2020 14.37

def read_file1():
    f = open("exception.py", "r", encoding="UTF-8")
    #print(f.read())  # 一次性读取所有内容，文件很大时会占用很大内存
    print(f.read(10)) # 指定大小的读取

    while True:
        z = f.read(10)
        print(z)
        if z is "":     # 如果结束了，不能接着读了
            break

    f.close()

# read_file1()

# with open 帮我们自动关闭文件的输入输出流
def read_file2(filename:str):
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(lines)


#read_file2("exception.py")

def read_file3(filename: int = -1) -> "explain":
    print(filename)
    print(read_file3.__annotations__)
    read_file3.__annotations__["info"] = "动态注释"
    print(read_file3.__annotations__)


# read_file3("aaa")
# read_file3()

def write_file():
    with open("1.txt", "w", encoding="UTF-8") as f:
        for i in range(100):
            f.write(str(i))
            f.flush()   # 将内存（缓冲区）的数据刷到磁盘上


write_file()