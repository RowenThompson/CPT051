#constants and definitions
LENGTH_RESTRICTION = .50

TOY_NAME_1 = "Toy Truck"
TOY_NAME_2 = "Toy House"

def display_welcome():
    print("Welcome")

def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

def display_toy_prompt():
    print("What toy do you want?")
    print("A.)" + TOY_NAME_1)
    print("B.)" + TOY_NAME_2)

#start

display_welcome()

#userName = input("User = ")

#print("Thank you, " + userName)

length = float(input("length = "))
width = float(input("Width = "))

sqft = length * width

print(sqft)
print(length)
print(width)


print(str(length) + " * " + str(width) + " = " + str(sqft))

display_toy_prompt()

menuSelection = take_input()

if(menuSelection == 'A'):
    print("A")
else:
    print("B")


