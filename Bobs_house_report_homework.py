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
uncoveredSquareFootage = houseSquareFootage - coveredSquareFootage
#------------------------------------------------------------
#start of report
print("------------------------------------------------------")
print("Welcome To Bob's House Report")
print("------------------------------------------------------")
#the report about the customer's house
#Username
print("Username:" + str(userName))
#Property Length
print("Property Length:" + str(propertyLength) + " ft.")
#Property Width
("Property Square Footage:" + str(propertySquareFootage) + " ft.")
#House Length
("House Length:" + str(houseLength) + " ft.")
#House Width
print("House Width:" + str(houseWidth) + " ft.")
#Pool Length
print("Pool Length:" + str(poolLength) + " ft.")
#Pool Width
print("Pool Width:" + str(poolWidth) + " ft.")
#-------------------------------------------------
#In total
#Covered Spuare Footage
print("Covered Square Footage:" + str(coveredSquareFootage) + " sq. ft.")
#Uncovered Square Footage
print("Uncovered Square Footage:" + str(uncoveredSquareFootage) + " sq. ft.")
#----------------------------------------------------------
print("Good bye!")
#End of report
