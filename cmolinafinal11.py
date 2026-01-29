#Ceiry Molina 
#Final Question 1

#coding part with the menu options

print("Menu Options for today")
print("._._._._._._._._._._._._.")
print("Option 1")
print("Option 2")
print("Option 3")
print("._._._._._._._._._._._._.")

x = int(input())

if x == 1: 
    name = input("Hello there, what is your name:")
    print(name, "Do you know whats a sharks favorite word?!? Its man OVERBOARD!!")
elif x==2:
    for i in range(20):
        print("pupusas")
elif x ==3: 
    x=10

    while (x!=0):
        x = float(input("Guess my number if you can loser!Its between 0-10"))
        if (x>0):
            print("Warning Warning Warning danger zone!!")
        elif (x <0):
            print("Warning Warning Warning Danger zone!!")
        else: 
            print("You guessed correctly loser! You won a million dollars")




