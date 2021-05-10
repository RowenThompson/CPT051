TAX_RATE = .075
DISCOUNT_NAME_MEMBER = 'Member'
DISCOUNT_NAME_SENIOR = 'Senior'
DISCOUNT_NAME_NONE = 'No Discount'
DISCOUNT_NAME_QUIT = 'quit'
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.25
DISCOUNT_RATE_NONE = 0.0
ITEM_NAME_PREMIUM = 'Ultra Size Bag of Eggs'
ITEM_NAME_SPECIAL = 'Standard Size Bag of Eggs'
ITEM_NAME_BASIC = 'Small Size Bag of Eggs'
ITEM_PRICE_PREMIUM = 55.95
ITEM_PRICE_SPECIAL = 24.95
ITEM_PRICE_BASIC = 15.95
DISCOUNT_MEMBER = ''
discountPrice = 0.0
itemSelection = ''

def show_discount_menu():
    print("This is the Discount Rate Menu.")
    print("A.) Member = " + str(DISCOUNT_RATE_MEMBER))
    print("B.) Senior = " + str(DISCOUNT_RATE_SENIOR))
    print("C.) None = " + str(DISCOUNT_RATE_NONE))
    print("Q.) Quit Program")

def show_item_menu():
    print("This is the Item Menu.")
    print("A.) " + ITEM_NAME_PREMIUM + ' = $' + str(ITEM_PRICE_PREMIUM))
    print("B.) " + ITEM_NAME_SPECIAL + ' = $' + str(ITEM_PRICE_SPECIAL))
    print("C.) " + ITEM_NAME_BASIC + ' = $' + str(ITEM_PRICE_BASIC))

def error_message():
    print("This is an invalid selection.")

#start
print("Welcome to the Carolinian Ice Palace!")
userName = input("Username= ")

show_discount_menu()


rateSelection = input("Rate Selection= ")

rateSelection = rateSelection.upper()
rateSelection = rateSelection[0]

while((rateSelection != 'A') and (rateSelection != 'B') and (rateSelection != 'C') and (rateSelection != 'Q')): #decision
    error_message()

if(rateSelection == 'A'):
    discountRate = DISCOUNT_RATE_MEMBER

elif(rateSelection == 'B'):
    discountRate = DISCOUNT_RATE_SENIOR

elif(rateSelection == 'Q'):
    print("Have a nice day!")
    exit()
else:
    discountRate = DISCOUNT_RATE_NONE

show_item_menu()

itemSelection = input("Item Selection= ")

itemSelection = itemSelection.upper()
itemSelection = itemSelection[0]

howMany = float(input("How Many= "))

if(itemSelection == 'A'):
    itemName = ITEM_NAME_PREMIUM
    itemPrice = ITEM_PRICE_PREMIUM

elif(itemSelection == 'B'):
    itemName = ITEM_NAME_SPECIAL
    itemPrice = ITEM_PRICE_SPECIAL

else:
    itemName = ITEM_NAME_BASIC
    itemPrice = ITEM_PRICE_BASIC

discountAmount = itemPrice * discountRate
discountPrice = itemPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

itemPrice_format = "{:.2f}".format(itemPrice)
discountAmount_format = "{:.2f}".format(discountAmount)
discountPrice_format = "{:.2f}".format(discountPrice)
howMany_format = "{:.0f}".format(howMany)
subTotal_format = "{:.2f}".format(subTotal)
tax_format = "{:.2f}".format(tax)
totalCost_format = "{:.2f}".format(totalCost)

print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("ORDER REPORT")
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("User                " + userName)
print("Item Name           " + itemName)
print("Original Price      " + '$  ' + str(itemPrice_format))
print("Discount            " + '   ' + str((discountRate * 100)) + '%' )
print("Discount Amount     " + '$  ' + str(discountAmount_format))
print("Discounted Price    " + '$  ' + str(discountPrice_format))
print("Quantity            " + '   ' + str(howMany_format))
print("SubTotal            " + '$  ' + str(subTotal_format))
print("Tax                 " + '$  ' + str(tax_format))
print("Total Cost          " + '$  ' + str(totalCost_format))
