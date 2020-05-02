# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 01/05/2020 15.50

"""
异常：运行的时候发生了错误，其实是代码抛出了一个错误
BaseException是所有异常的基类
异常的处理方式：
try:
    代码块
except 异常名字:
    代码块 （如何处理异常）
else:
    代码块
"""

# ###############################
# # eg.1
# try:
#     #file = open("aaaa","r")
#     i = 1
# except:
#     print("Error happen")
# else:
#     print("no error")


# ##############################
# # eg.2
# try:
#     file = open("aaaa","r")
#     # i = 1
# except FileNotFoundError as e:
#     print("Error happen: file not found")
#     print(e)
# else:
#     print("no error")


# ############################
# # eg.3
# try:
#     file = open("aaaa","r")
#     # i = 1
# # except Exception:
# #     print("发生异常了")
# #except FileNotFoundError as e:
# #     print("Error happen: file not found")
# #     print(e)
# except ReferenceError as e:
#     print("Error 2")
# except Exception:       #权限大的异常放后边
#     print("发生异常了")
# else:
#     print("no error")
# finally:
#     print("this will be print anyway")

"""
异常的处理原则：
你能处理的再捕获，不能处理就抛出
"""
# ######################
# # 手动抛出异常
# try:
#     raise Exception("手动抛出异常")    # 括号里为异常信息
# except:
#     print("catch an error")


# 自定义异常
class MyDefineError(BaseException):
    pass

try:
    raise MyDefineError("through an error")
except MyDefineError as e:
    print(e)


