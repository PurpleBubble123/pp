
"""
正则表达式的高级应用
贪婪与非贪婪
非贪婪：尽可能少的匹配 操作符：? ，可用在 * + ？ 后
  *?
  +?
  ??
"""
import  re

# s = "aaiiiiiii"
# #reg = "aai*"
# #reg = "aai*?"
# #reg = "aai+?"
# reg = "aai??"
#
# print(re.findall(reg,s))

"""
分支条件匹配
操作符:|
"""

# s = "my number: 010-83795088 0210-98787284 0451-8888888"
# #reg = "0\d{2}-\d{8}"
# #reg = "0\d{3}-\d{7}"
# reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}"
# print(re.findall(reg,s))

"""
零宽断言
(?=reg)  匹配reg前边的位置
(?<=reg)  匹配reg后边的位置
(?!=reg)  匹配后边跟的不是reg的位置
(?<!
reg)  匹配后边跟的不是reg的位置


"""

s = "kjsiskkyifetokky"
# reg = "k{2}y(?=ife)"
# print(re.findall(reg,s))

reg = "(?<=jsis)[a-z]*"
print(re.findall(reg,s))


