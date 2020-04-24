
import  aiml

k = aiml.Kernel()
k.learn("std-startup2.xml")
k.respond("load aiml b")

while True:
    answer = k.respond(input("input>>"))
  #  a = answer.replace(" ", "")
 #   a = answer.replace(" ","")
    print(answer)

