s=input("please enter your password :: ")
Password = str( 'as1987Jantu35*^ft$TTTdyuHi28Mary')
if (s == Password): 
    print("You have successfully entered the correct password")
while (s != Password):
    print("Hint:1 The length of your password is 32 characters")
    s=input("please enter your password :: ")
    if(s!= Password):
        print("Your password has 8 numbers")
        s= input("please enter your password :: ")
        if (s!= Password):
            print("Your password has 1 i in it")
    if (s == Password):
        break
print("You successfully entered the correct password")

               

