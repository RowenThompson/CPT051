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

userName = input("Username = ")
propertyLength = float(input("Property Length = "))
propertyWidth = float(input("Property Width = "))

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

elif(waterVolume <= HEATER_CAP_B):
    heaterName = HEATER_NAME_B

elif(waterVolume <= HEATER_CAP_C):
    heaterName = HEATER_NAME_C   
  
else:
    heaterName = HEATER_NAME_D
    heaterName = HEATER_NAME_E


sodCost_format = "{:.2f}".format(sodCost)
waterVolume_format = "{:.1f}".format(waterVolume)
coveredSquareFootage_format = "{:.1f}".format(coveredSquareFootage)
uncoveredSquareFootage_format = "{:.1f}".format(uncoveredSquareFootage)

print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print(userName + 's' + " Property Report.")
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Property Length                  " + str(propertyLength) + ' ft')
print("Property Width                   " + str(propertyWidth) + ' ft')
print("Property Area                    " + str(propertySquareFootage) + ' sq.ft.')
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Design Length Restriction        " + str((LENGTH_RESTRICTION * 100)) + ' %' )
print("Design Width Restriction         " + str((WIDTH_RESTRICTION * 100)) + ' %' )
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("House Length                     " + str(houseLength) + ' ft')
print("House Width                      " + str(houseWidth) + ' ft')
print("House Area                       " + str(houseSquareFootage) + ' sq.ft.')
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Pool Length                      " + str(poolLength) + ' ft')
print("Pool Width                       " + str(poolWidth) + ' ft')
print("Pool Area                        " + str(poolSquareFootage) + ' sq.ft.')
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Pool Volume                      " + str(waterVolume) + ' cu.ft.')
print("Heater Unit                      " + heaterName)
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Covered Area                     " + str(coveredSquareFootage_format))
print("Uncovered Area                   " + str(uncoveredSquareFootage_format))
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
print("Sod Name                         " + sodName)
print("Sod Price (per sq.ft.)           " + str(sodPrice))
print("Sod Cost                         " + CURRENCY + str(sodCost_format))
print("~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~ ~~~~")
