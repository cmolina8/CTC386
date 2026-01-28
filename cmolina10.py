#Ceiry Molina 
#Final Project Lab 10

#Celcius Function Part 

def celsiusfunction():
    y = int(input(print("Please enter the current temparture in Fahenheit degress.\n")))
    celsius = (y - 32) * (5/9)
    print("The temperature in degrees Celsius is:", celsius, "loser") 

def pumpkinpie_size():
    r = int(input("How big do you want your pie? This is a custom pumpkin pie parlor so please enter the size of the radius in inches \n"))
    pumpkinpie_area = 3.14*(r**2)
    if (pumpkinpie_area < 20):
            print("This pumpkin pie is small, we might have to order 2 loser!")
    elif((pumpkinpie_area >=20) and (pumpkinpie_area <=80)):
                print("I think we can eat this pie between the two of us, just the two of us")
    elif(pumpkinpie_area > 80):
                print("this is a job is meant for more than 2 people loser!!")
                

#coding part with the menu option 
name = input("Hello there, what is your name:")

print("Menu Options for today")
print("._._._._._._._._._._._._.")
print("Option 1")
print("Option 2")
print("Option 3") 
print("Option 4")
print("Option 5")
print("Option 6")
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

elif x==6:
    i = 10
    while ( i not in range(3)):
        i = int(input("Are you in the mood for some pumpkin pie? Enter 1 for yes or 2 for no"))
    if ( i == 2):
        print("Fine, I'll just eat a pumpkin pie by myself then loser!!")
    elif ( i == 1):
           pumpkinpie_size()



