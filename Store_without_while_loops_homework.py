DISCOUNT_RATE = 0.25
print("Welcome")

userName = input("Username: " )
itemName = input("Itemname: " )
howMany = float(input("Howmany: "))
originalPrice = float(input("Price: "))


discountAmount = originalPrice * DISCOUNT_RATE
discountPrice = originalPrice - discountAmount
totalCost = howMany * discountPrice
print()
print("Recepit")
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
print("total cost " + str(totalCost))

print("Bye")


