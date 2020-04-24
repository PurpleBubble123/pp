"""
|正则表达式是用来操作字符串的一种逻辑公式
"""

import  re

# # eg.1
# s = "webset: http://www.baidu.com"
# reg = "http://[w]{3}\.[a-z0-9]*\.com"
#
# result = re.findall(reg,s)
# print(result)
#
# # eg.2
# s = "hello world hello"
# reg = "hello"
#
# print(re.findall(reg,s))
# print(re.findall(reg,s)[0])

# 元字符
"""
. 代表换行符以外的任意字符  \n
\w 匹配字母/number/_/汉字
\s 匹配任意空白符
\d 匹配任意的数字 0-9
^ 匹配字符串的开始
$ 匹配字符串的结束
"""

# s = "23sgrdg工人    房356#￥%__"
# print(re.findall("\w",s))
# print(re.findall("\d",s))
# print(re.findall("\s",s))
# print(re.findall("^\d",s))

# 反义代码
"""
\W : not \w
\S : not \s
\D : not \d
"""

# 限定符
"""
# s = "webset: http://www.baidu.com"
# reg = "http://[w]{3}\.[a-z0-9]*\.com"
[]* : 代表它前面的正则表达式重复0次或多次
+ : 重复一次或多次
? : 重复0次或1次 
{n} : 重复n次
{n,}: 重复n次或多次，至少重复n次
{n,m}: 重复n次到m次
"""

# s = "hhhhhh sd123父官5555....sjjdo"
# print(re.findall("\d{3}",s))
# print(re.findall("[\da-z]*",s))
# print(re.findall("[\da-z]+",s))
# print(re.findall("[\da-z]?",s))

# s1 = "my qq is 3465513"
# reg = "\d{5,12}"
# print(re.findall(reg,s1))

# 分组匹配
s =  "my qq is 3465513, mail:10000"
reg = "(\d{7}).*(\d{5})"
print(re.findall(reg,s))
print(re.search(reg,s))
print(re.search(reg,s).group())
print(re.search(reg,s).group(2)) # 组2的内容
print(re.search(reg,s).group(1)) # 组一的内容
print(re.search(reg,s).group(0)) # 匹配的所有内容


















