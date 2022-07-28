
while True:
    x = input("Which HOMEWORK you want to check? \n \
    If you are interested in the HW №1 prees \"1\"\n \
    If you are interested in the HW №2 prees \"2\"\n \
    If you want to exit - press any other key\n \
    Your choise  is:")
    
    if x == "1":
        name = input("What is your name?\n")
        age = input("How old are you?\n")
        adress = input("Where do you living?\n")

        print("Hello, ", name )
        print("Your age is ", age)
        print("You live in ", adress)   

    if x == "2":  
        a=int(input("Enter number \"a\" \na="))
        b=int(input("Enter number \"b\"\n b="))

        print(
            "a=", a, "\n" 
            "b=", b, "\n" 
            "a+b=", a+b, "\n" 
            "a-b=", a-b, "\n" 
            "a*b=", a*b, "\n" 
            "a/b=", a/b, "\n" 
            "a**b=", a**b, "\n") 
    
    else: break

print("GOODBYE")




