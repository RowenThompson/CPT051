DISCOUNT_NAME_MEMBER = 'Member'
DISCOUNT_NAME_SENIOR = 'Senior'
DISCOUNT_NAME_NONE = 'No Discount'
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.25
DISCOUNT_RATE_NONE = 0.0
TAX_RATE = .075

menuSelection = 'U'
discountRate = (float('.0'))
print("Welcome")

userName = str(input("userName = "))
itemName = str(input("itemName = "))
originalPrice = float(input("originalPrice = "))
howMany = float(input("howMany = "))
menuSelection = input("menuSelection = ")
#def take_input():
    #print("Enter your selection here")
    #selection = input()
    #selection = selection.upper()
    #selection = selection[0]
    #return selection

if(menuSelection == 'A'):
    print("Hello Member")
    discountRate = DISCOUNT_RATE_MEMBER
    #menuSelection.append('B')
    
elif(menuSelection == 'B'):
    print("Hello Senior")
    discountRate = DISCOUNT_RATE_SENIOR
    #menuSelection.append('B')
    
else:
    print("No Discount")
    DiscountRate = DISCOUNT_RATE_NONE
    #menuSelection.append('Something')
discountAmount = originalPrice * discountRate
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

if(totalCost > 0.0):
    print("User: " + str(userName))
    print("itemName: " + str(itemName))
    print("originalPrice: " + str(originalPrice))
    print("discountRate: " + str(discountRate))
    print("discountAmount: " + str(discountAmount))
    print("discountPrice:" + str(discountPrice))
    print("howMany: " + str(howMany))
    print("subTotal: " + str(subTotal))
    print("tax: " + str(tax))
    print("totalCost: " + str(totalCost))

#take_input()

print(menuSelection)
