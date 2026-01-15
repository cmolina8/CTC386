#Ceiry Molina 
#Final Project Lab 9
#GitHub Test Comment

#Celcius Function Part 

def celsiusfunction():
    y = int(input(print("Please enter the current temparture in Fahenheit degress.\n")))
    celsius = (y - 32) * (5/9)
    print("The temperature in degrees Celsius is:", celsius, "loser") 

#coding part with the menu option 
name = input("Hello there, what is your name:")

print("Menu Options for today")
print("._._._._._._._._._._._._.")
print("Option 1")
print("Option 2")
print("Option 3") 
print("Option 4")
print("Option 5")
print("._._._._._._._._._._._._.")

print("Hello there", name, "Enter an option")
x = int(input())

if x == 1: 
    print("What did the bufflo say to his son when he college?")
    print("Bison!")
elif x==2:
    for i in range(15):
        print(name)
elif x ==3: 
    num = int(input("Enter a number:"))
    for i in range(num):
        print("With great power comes great resposiblity")
elif x==4:

    x=0
    while (x!=59):
        x = float(input("Guess my number if you can loser!Its between 0-100"))
        if (x>=0) and (x<=58):
            print("Your guess is too low try again")
        elif (x>=59) and (x<=100): 
            print("Your guess is too high try again")
        else: 
            print("Out of range, please enter a number in range")
    print("You guessed correctly loser! You won a million dollars!")

elif x==5:
    celsiusfunction() 



