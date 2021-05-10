TAX_RATE = .075
DISCOUNT_NAME_MEMBER = 'Member'
DISCOUNT_NAME_SENIOR = 'Senior'
DISCOUNT_NAME_NONE = 'No Discount'
DISCOUNT_NAME_QUIT = 'quit'
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.25
DISCOUNT_RATE_NONE = 0.0
ITEM_NAME_PREMIUM = ''
ITEM_NAME_SPECIAL = ''
ITEM_NAME_BASIC = ''
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

def error_message():
    print("This is an invalid selection.")

#start
print("Welcome!")
userName = input("userName= ")

show_discount_menu()

rateSelection = input("rateSelection= ")

while((rateSelection != 'A') and (rateSelection != 'B') and (rateSelection != 'C') and (rateSelection != 'Q')): #decision
    error_message()

if(rateSelection == 'A'):
    discountRate = DISCOUNT_RATE_MEMBER

elif(rateSelection == 'B'):
    DiscountRate = DISCOUNT_RATE_SENIOR

elif(rateSelection == 'Q'):
    print("Have a nice day!")
    exit()
else:
    discountRate = DISCOUNT_RATE_NONE

howMany = float(input("howMany= "))

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
totalCost = subTotal - tax

print("Receipt= ")
print(userName)
print(itemName)
print(itemPrice)
print(discountRate)
print(discountAmount)
print(discountPrice)
print(howMany)
print(subTotal)
print(tax)
print(totalCost)
