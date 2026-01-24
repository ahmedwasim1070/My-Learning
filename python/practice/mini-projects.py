# Guess The Number

# import random
# num=random.randint(1,10)
# while True:
#    rdmNum=input("Guess the Number or Enter Q to Quit:")
#    if(rdmNum=="Q" or rdmNum=="q"):
#       print("You Quitted the Game!")
#       break
#    try:
#       guessNum=int(rdmNum)
#    except:
#       print("You can only write  string(Q/q) or Numbers")
#       continue
#    if(guessNum>10 or guessNum<=0):
#       print("Enter the Number Under the 1 to 10")
#    elif(guessNum==num):
#       print("congradulation you won the game")
#       break
#    else:
#       print("Your Guess was wrong")

# Random Passwrod Generator
# import random
# import string

# Allval=string.ascii_letters + string.digits + string.punctuation
# print(Allval)
# pas=""
# for i in range(14):
#    idxnum=random.randint(0,len(Allval))
#    newVal=Allval[idxnum]
#    pas+=newVal
# print("Your Password is:" ,pas)

# with open("password.txt","a+") as f:
#    f.write("\n Your Passwords=")
#    addPass=f.write(pas)

# or 
# import random 
# import string

# Allval=string.ascii_letters + string.digits + string.punctuation
# passwrod=""
# for i in range (12):
#    passwrod+=random.choice(Allval)
# print("Your Strong Random passwrod is:",passwrod)


# or
# import random 
# import string

# allval=string.ascii_letters +string.digits+string.punctuation
# password="".join([random.choice(allval) for i in range(12)])
# print(password)
