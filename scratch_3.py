#ask user would like they to know their balance
print("hello user")
question= input("would you like to determine how much you owe your mobile phone provider based on your subscription? y/n \n")
#if and elif statement if they say yes prompt the packages if no end program
if question.lower()=="no" or question.lower()=="n":
    print("goodbye")
    exit()

elif question.lower()=="yes" or question.lower()=="y":
    #prompt user to the packages
    print("Green: 2GB of data for $49.99/month. Additional GB are $14.99/GB.")
    print("Orange:4GB of data for $69.99/month. Additional GB are $9.99/GB")
    print("Purple:$99.99/month for unlimited data.")
#input package
    package = (input("enter the package \n"))
    package = package.lower()
    if (package !="green" and package != "orange" and package!= "purple"):
        print("invalid package")
    else:
        usage = float(input("enter the usage (How many GB have you used? \n"))
        if usage < 0:
            print("you need to enter a valid number")
        else:
            if package ==("purple"):
                cost= 99.99
            else:
                if package== ("orange"):
                    if (usage >= 4):
                        cost= 69.99 + (usage-4) * 9.99
                    else:
                        cost=69.99
                        # green --requires coupon there is a further discount of $20 on bills that are $75 or more.
                else:
                    if package==("green"):
                        if (usage >=2):
                            cost=49.99 + (usage-2) * 14.99

                            if (cost>=75):
                                cost = cost-20

                        else:
                            cost = 49.99

print('You owe: $' + str(cost))
