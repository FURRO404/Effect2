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
    double = random.randint(0, 2) #Get random number to choose for a double character instance.
    
    if double == 0:
        mix = random.randint(0, 100) #100 is maximum distance for line length.
        
        for i in range(0, mix):
            line.append(" ") 

        choices = [".", "/", ">", "#", "@", "*", "%", "<"] #List of choices for character to be.
        choice = random.choice(choices)
        line.append(choice)
        
        print(listconv(line))
        time.sleep(0.001)
        line.clear()

    elif double == 1:
        for i in range(0, 2):
            mix = random.randint(0, 50) #Lowered to 50 so line can never exceed 100.
            
            for i in range(0, mix):
                line.append(" ")
                
            choices = [".", "/", ">", "#", "@", "*", "%", "<"] #List of choices for character to be.
            choice = random.choice(choices)
            line.append(choice)
            
        print(listconv(line))
        time.sleep(0.001)
        line.clear()
        
    elif double == 2:
        for i in range(0, 3):
            mix = random.randint(0, 33) #Lowered to 33 so line can never exceed 100.
            
            for i in range(0, mix):
                line.append(" ")
                
            choices = [".", "/", ">", "#", "@", "*", "%", "<"] #List of choices for character to be.
            choice = random.choice(choices)
            line.append(choice)
            
        print(listconv(line))
        time.sleep(0.001)
        line.clear()
#=============FURRO404=============#
