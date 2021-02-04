for i in range(1,6):
    for j in range(1,10):
        if(i+j==6)|(j-i==4):
            print("*",end="")
        elif(i==5):
            print("*",end="")
        else:
            print(" ",end="")

    print("")