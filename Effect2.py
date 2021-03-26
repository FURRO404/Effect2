#=============FURRO404=============#
#Effect2.py
import random
import time
#------------------#
line = []

def listconv(line):
    str1 = " "
    return (str1.join(line))

while True:
    mix = random.randint(0, 100)
    for i in range(0, mix):
        line.append(" ")

    choices = [".", "/", ">", "#", "@", "*", "%", "<"]
    choice = random.choice(choices)
    
    line.append(choice)
    print(listconv(line))
    time.sleep(0.001)
    line.clear()
#=============FURRO404=============#
