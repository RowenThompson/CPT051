LENGTH_RESTRICTION = .50
WIDTH_RESTRICTION = .75
SOD_NAME_A = "South Carolina Rye"
SOD_NAME_B = "Kentucky Bluegrass"
SOD_PRICE_A = .57
SOD_PRICE_B = 1.47
HEATER_NAME_A = "Unit A3100"
HEATER_NAME_B = "Unit B8000"
HEATER_NAME_C = "Unit C15000"
HEATER_NAME_D = "Unit D25000"
HEATER_NAME_E = "Unit E25000+"
HEATER_CAP_A = 3100.0
HEATER_CAP_B = 8000.0
HEATER_CAP_C = 15000.0
HEATER_CAP_D = 25000.0
POOL_DEPTH = 6

def welcomeBanner():
    print("Welcome!")

def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

#start

#welcomeBanner()

#userName = input("userName = ")
propertyLength = float(input("propertyLength = "))
propertyWidth = float(input("propertyWidth = "))

propertySquareFootage = propertyLength * propertyWidth
houseLength = propertyLength * LENGTH_RESTRICTION
houseWidth = propertyWidth * WIDTH_RESTRICTION
houseSquareFootage = houseLength * houseWidth
poolLength = houseLength * LENGTH_RESTRICTION
poolWidth = houseWidth * WIDTH_RESTRICTION



#print(type(userName))
#print(type(propertyLength))
#print(type(propertyWidth))
#print(type(propertySquareFootage))
#print(type(LENGTH_RESTRICTION))
#print(type(houseLength))
#print(type(WIDTH_RESTRICTION))
#print(type(houseWidth))



#print(userName)
#print(str(propertyLength))
#print(str(propertyWidth))
#print(str(propertySquareFootage))
#print(str(propertyLength))
#print(LENGTH_RESTRICTION)
#print(houseLength)
print(WIDTH_RESTRICTION)
print(houseWidth)
#print(houseSquareFootage)
#print(poolLength)
print(poolWidth)
