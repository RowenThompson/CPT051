DISCOUNT_NAME_MEMBER = "Member"
DISCOUNT_NAME_SENIOR = "Senior"
DISCOUNT_NAME_NONE = "No Discount"
DISCOUNT_RATE_MEMBER = 0.15
DISCOUNT_RATE_SENIOR = 0.25
DISCOUNT_RATE_NONE = 0.0
TAX_RATE = .075
print("Welcome")
userName = str(input("userName= "))
itemName = str(input("itemName= "))
originalPrice = float(input("originalPrice= "))
howMany = float(input("howMany= "))
menuSelection = str(input("menuSelection= "))

if(menuSelection == 'A'):
    print("Welcome back member!")
    discountRate = DISCOUNT_RATE_MEMBER

elif(menuSelection == 'B'):
    print("You selected B")
    discountRate = DISCOUNT_RATE_SENIOR

else:
    print("LOL YOU SUCK")
    discountRate = DISCOUNT_RATE_NONE

discountAmount = originalPrice * discountRate
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

print(str((discountRate * 100)) + "%" )

if(totalCost > 0.0):
    print(str("User              " + userName))
    print(str("Item Name         " + itemName))
    print(str("Original Price   $" + originalPrice))
    print(str(("Discount         " + discountRate * 100)) + "%" )
    print(str(discountAmount))
    print(str(discountPrice))
    print(str(howMany))
    print(str(subTotal))
    print(str(tax))
    print(str(totalCost))
print("Good bye!")
print(discountRate)
