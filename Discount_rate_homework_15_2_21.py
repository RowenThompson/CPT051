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
originalPrice = str(input("originalPrice= "))
howMany = str(input("howMany= "))
menuSelection = str(input("menuSelection= "))

if(menuSelection == 'A'):
    print("You selected A")
    discountRate = DISCOUNT_RATE_MEMBER
elif(menuSelection == 'B'):
    print("You selected B")
    if(menuSelection == 'N'):
        discountRate = DISCOUNT_RATE_NONE
    elif(menuSelection == 'Y'):
        discountRate = DISCOUNT_RATE_SENIOR

discountAmount = originalPrice * DISCOUNT_RATE
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

print(str((discountRate * 100)) + "%" )

if(totalCost > 0.0):
    print(userName)
    print(itemName)
    print(originalPrice)
    print(discountRate)
    print(discountAmount)
    print(discountPrice)
    print(howMany)
    print(subTotal)
    print(tax)
    print(totalCost)
print("Good bye!")
