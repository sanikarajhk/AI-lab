dirt=input("is there dirt?(y/n)")
front=input("is there wall in front?(y/n)")
right=input("is there wall at right?(y/n)")
left=input("is there wall at left?(y/n)")
if(dirt=="y"):
    print("suck dirt")
elif(front=="n"):
    print("move forward")
elif(right=="n"):
    print("move right")
elif(left=="n"):
    print("move left")
else:
    print("turn around")
 
