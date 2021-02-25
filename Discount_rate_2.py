DISCOUNT_NAME_MEMBER = 'Member'
DISCOUNT_NAME_SENIOR = 'Senior'
DISCOUNT_NAME_NONE = 'No Discount'
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.25
DISCOUNT_RATE_NONE = 0.0
TAX_RATE = .075
discountRate = 0
menuSelection = n
print("Welcome")

def take_input():
    print("Enter your selection here")
    menuSelection = input()
    menuSelection = menuSelection.upper()
    menuSelection = menuSelection[0]
    return selection

userName = str(input("userName = "))
itemName = str(input("itemName = "))
originalPrice = float(input("originalPrice = "))
howMany = float(input("howMany = "))
#menuSelection = str(input("menuSelection = "))

def take_input():
    menuSelection = menuSelection.upper()
    menuSelection = menuSelection[0]
    return selection


if(menuSelection == 'A'):
    print("Hello Member")
    discountRate = DISCOUNT_RATE_MEMBER

elif(menuSelection == 'B'):
    print("Hello Senior")
    discountRate = DISCOUNT_RATE_SENIOR

else:
    print("No Discount")
    DiscountRate = DISCOUNT_RATE_NONE

discountAmount = originalPrice * discountRate
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

if(totalCost > 0.0):
    print(userName)
    
take_input()
