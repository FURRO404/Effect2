#=============FURRO404=============#
#Effect2.py
import random
import time
#------------------#
def listconv(line):
    str1 = " "
    return (str1.join(line))

line = []

while True:
    double = random.randint(0, 1)
    
    if double == 0:
        mix = random.randint(0, 100)
        for i in range(0, mix):
            line.append(" ")

        choices = [".", "/", ">", "#", "@", "*", "%", "<"]
        choice = random.choice(choices)
        line.append(choice)
        
        print(listconv(line))
        time.sleep(0.001)
        line.clear()

    if double == 1:
        for i in range(0, 2):
            mix = random.randint(0, 50)
            for i in range(0, mix):
                line.append(" ")
                
            choices = [".", "/", ">", "#", "@", "*", "%", "<"]
            choice = random.choice(choices)
            line.append(choice)
            
        print(listconv(line))
        time.sleep(0.001)
        line.clear()
#=============FURRO404=============#
