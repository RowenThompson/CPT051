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
CURRENCY = '$'



def welcomeBanner():
    print("Welcome!")

def sod_menu():
    print("/// MENU ///")
    print("A). " + SOD_NAME_A + ' = ' + CURRENCY + str(SOD_PRICE_A))
    print("B). " + SOD_NAME_B + ' = ' + CURRENCY + str(SOD_PRICE_B))    
def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

#start

#welcomeBanner()


propertyLength = float(input("propertyLength = "))
propertyWidth = float(input("propertyWidth = "))

propertySquareFootage = propertyLength * propertyWidth
houseLength = propertyLength * LENGTH_RESTRICTION
houseWidth = propertyWidth * WIDTH_RESTRICTION
houseSquareFootage = houseLength * houseWidth
poolLength = houseLength * LENGTH_RESTRICTION
poolWidth = houseWidth * WIDTH_RESTRICTION
poolSquareFootage = poolLength * poolWidth
coveredSquareFootage = houseSquareFootage + poolSquareFootage
uncoveredSquareFootage = propertySquareFootage - coveredSquareFootage
sod_menu()

menuSelection = take_input()

if(menuSelection == 'A'):
    sodName = SOD_NAME_A
    sodPrice = SOD_PRICE_A

else:
    sodName = SOD_NAME_B
    sodPrice = SOD_PRICE_B

sodCost = uncoveredSquareFootage * sodPrice
waterVolume = poolSquareFootage * POOL_DEPTH

if(waterVolume <= HEATER_CAP_A):
    heaterName = HEATER_NAME_A
    print("A and only A")

elif(waterVolume <= HEATER_CAP_B):
    heaterName = HEATER_NAME_B
    print("B and only B")

elif(waterVolume <= HEATER_CAP_C):
    heaterName = HEATER_NAME_C
    print("C and only C")    
  
else:
    
      
    






#print(menuSelection)
#print(sodName)
#print(sodCost)
#print(waterVolume)
#print("///////////////////////////")
waterVolume_format = "{:.1f}".format(waterVolume)
#print(waterVolume_format)
#print(type(waterVolume_format))



print("Pool Volume           " + str(waterVolume_format) + ' cu.ft.')
