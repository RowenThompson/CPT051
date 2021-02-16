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
    print("LOL")
    discountRate = DISCOUNT_RATE_NONE

discountAmount = originalPrice * discountRate
discountPrice = originalPrice - discountAmount
subTotal = howMany * discountPrice
tax = subTotal * TAX_RATE
totalCost = subTotal + tax

if(totalCost > 0.0):
    print("User              " + userName)
    print("Item Name         " + itemName)
    print("Original Price   $" + originalPrice)
    print(("Discount         " + discountRate * 100) + "%" )
    print("Discount Amount  $" + discountAmount)
    print("Discounted Price $" + discountPrice)
    print("Quantity          " + howMany)
    print("Subtotal         $" + subTotal)
    print("Tax              $" + tax)
    print("Total Cost       $" + totalCost)
print("Good bye!")

