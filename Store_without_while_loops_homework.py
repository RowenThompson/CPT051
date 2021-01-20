DISCOUNT_RATE = 0.25
print("Welcome")

userName = input("1" )
itemName = input("2" )
howMany = 2
originalPrice = 4


discountAmount = originalPrice * DISCOUNT_RATE
discountPrice = originalPrice - discountAmount
totalCost = howMany * discountPrice
print(discountAmount)
print(discountPrice)
print(totalCost)
print(userName)
print(itemName)
print(howMany)
print(originalPrice)
print(DISCOUNT_RATE)
print(discountAmount)
print(discountPrice)
print(totalCost)

print("Bye")

exit()
