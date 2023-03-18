userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ") 
if userReply == "stamps":
    print("we have many stamp designs to choose from")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("how many copies would you linke? (enter a number) ")
    print("Here are {} copies. ".format(copies))
else: print("thank you, please come again!!")