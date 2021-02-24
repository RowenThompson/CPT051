#Start
#----------------------------------------------------------
#To get the information
userName = input("UserName: ")
propertyLength = float(input("Property Length: "))
propertyWidth = float(input("Property Width: "))
houseLength = float(input("House Length: "))
houseWidth = float(input("House Width: "))
poolLength = float(input("Pool Length: "))
poolWidth = float(input("Pool Width: "))

def error_message():
    print("Invalid")
#-----------------------------------------------------------
#Getting the result for the customer
#Calculating then the result will be propertySquareFootage
propertySquareFootage = propertyLength * propertyWidth

#Calculating then the result will be houseSquareFootage
houseSquareFootage = houseLength * houseWidth

#Calculating then the result will be poolSquareFootage
poolSquareFootage = poolLength * poolWidth

#Calculating then the result will be coveredSquareFootage
coveredSquareFootage = houseSquareFootage + poolSquareFootage

#Calculating then the result will be uncoveredSquareFootage
uncoveredSquareFootage = propertySquareFootage - coveredSquareFootage
#------------------------------------------------------------
#start of report
print("```` ```` ```` ```` ```` ```` ```` ```` ```` ```` ````")
print("Welcome To Bob's House Report")
print("```` ```` ```` ```` ```` ```` ```` ```` ```` ```` ````")
#the report about the customer's house
#Username
print("Username:" + str(userName))
#Property Length
print("Property Length:" + str(propertyLength) + " ft.")
#Property Width
print("Property Length:" + str(propertyWidth) + " ft.")
#Property Area
print("Property Area:" + str(propertySquareFootage) + " sq.ft.")
#House Length
print("House Length:" + str(houseLength) + " ft.")
#House Width
print("House Width:" + str(houseWidth) + " ft.")
#House Area
print("House Area:" + str(houseSquareFootage) + " sq.ft.")
#Pool Length
print("Pool Length:" + str(poolLength) + " ft.")
#Pool Width
print("Pool Width:" + str(poolWidth) + " ft.")
#Pool Area
print("Pool Area:" + str(poolSquareFootage) + " sq.ft.")
#-------------------------------------------------
#In total
#Covered Spuare Footage
print("Covered Area:" + str(coveredSquareFootage) + " sq. ft.")
#Uncovered Square Footage
print("Uncovered Area:" + str(uncoveredSquareFootage) + " sq. ft.")
#----------------------------------------------------------
#End of report
