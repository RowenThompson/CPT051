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
propertyLength = str(propertyLength)
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
print("Username:" + userName)
#Property Length
print("Property Length:" + propertyLength + " ft.")
#Property Width
("Property Square Footage:" + propertySquareFootage + " ft.")
#House Length
("House Length:" + houseLength + " ft.")
#House Width
print("House Width:" + houseWidth + " ft.")
#Pool Length
print("Pool Length:" + poolLenght + " ft.")
#Pool Width
print("Pool Width:" + poolWidth + " ft.")
#-------------------------------------------------
#In total
#Covered Spuare Footage
print("Uncovered Square Footage:" + coveredSquareFootage + " sq. ft.")
#Uncovered Square Footage
print("Uncovered Square Footage:" + uncoveredSquareFootage + " sq. ft.")
#----------------------------------------------------------
print("Good bye!")
#End of report
