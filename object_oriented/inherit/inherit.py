# It is a nice day. Let's get start
__author__ = "boya"
__date__ = "27 / 04 / 2020"

class Father:
    name = "lilei"
    sex = "M"

    def __init__(self):
        print("father constructor function")

    def speak_english(self):
        print("father english")

    def __juehuo(self):
        print("father juehuo")

class Mother:
    name = "hanmeimei"
    sex = "F"
    def __init__(self):
        print("mother constructor")

    def speak_chinese(self):
        print("mother chinese")


class Child(Father,Mother):  # 如果要继承，必须写括号里
    #pass
    def __init__(self):
        print("Child constructor function")

    def speak_english(self):
        print("child english")

    def study(self):
        print("child study")




c = Child()
c.speak_english()
c.study()
c.speak_chinese()
print(Child.__bases__)

