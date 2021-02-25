def author_aig():
    print("Rowen Thompson")
    print("CPT051")
    print("Discount_rate_homework_15_2_21.py")
    print("Febuary 2021")
    print("------------------------")

originalPrice = 24.95
howMany = 4
discountRate = 0.0
menuSelection = 'S'
userName = 'Jill'
itemName = 'Flashlight'

DISCOUNT_NAME_MEMBER = "Member"
DISCOUNT_NAME_SENIOR = "Senior"
DISCOUNT_NAME_NONE = "No Discount"
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.75
DISCOUNT_RATE_NONE = 0.0
TAX_RATE = .075

def bye_end():
    print("Bye!")

def welcome_start():
    print("Hello and welcome!")

def error_message():
    print("This is an invalid selection.")

def questions_for_input():
    userName = str(input("userName = "))
    itemName = str(input("itemName = "))
    originalPrice = float(input("originalPrice = "))
    howMany = str(input("howMany = "))

def show_discount_menu():
    print("Select discount rate!")
    print("A)Member : " + str(DISCOUNT_RATE_MEMBER) + '%')
    print("B)Senior : " + str(DISCOUNT_RATE_SENIOR) + '%')
    print("C)None : " + str(DISCOUNT_RATE_NONE) + '%')

def menu_selection_input():
    menuSelection = str(input("menuSelection = "))
    if(menuSelection == 'A'):
        print("You selected Member!")
        discountRate = DISCOUNT_RATE_MEMBER

    elif(menuSelection == 'B'):
        print("You selected Senior")
        discountRate = DISCOUNT_RATE_SENIOR

    else:
        print("You selected None")
        discountRate = DISCOUNT_RATE_NONE

discountAmount = originalPrice * discountRate
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax


if(totalCost > 0.0):
    print("User              " + str(userName))
    print("Item Name         " + str(itemName))
    print("Original Price   $" + str(originalPrice))
    print(("Discount         " + str(discountRate * 10) + "%" ))
    print("Discount Amount  $" + str(discountAmount))
    print("Discounted Price $" + str(discountPrice))
    print("Quantity          " + str(howMany))
    print("Subtotal         $" + str(subTotal))
    print("Tax              $" + str(tax))
    print("Total Cost       $" + str(totalCost))

def info_receipt():
    print("User              " + str(userName))
    print("Item Name         " + str(itemName))
    print("Original Price   $" + str(originalPrice))
    print(("Discount         " + str(discountRate * 100) + "%" ))
    print("Discount Amount  $" + str(discountAmount))
    print("Discounted Price $" + str(discountPrice))
    print("Quantity          " + str(howMany))
    print("Subtotal         $" + str(subTotal))
    print("Tax              $" + str(tax))
    print("Total Cost       $" + str(totalCost))

author_aig()

questions_for_input()

show_discount_menu()

menu_selection_input()

info_receipt()
