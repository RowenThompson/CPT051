#s
#Start
#Bobs house report
print("Hello this is you're house report!")
#----------------------------------------------------------
#To get the information
userName = input("UserName: ")
propertyLength = float(input("propertyLength: "))
propertyWidth = float(input("propertyWidth: "))
houseLength = float(input("houseLength: "))
houseWidth = float(input("houseWidth: "))
poolLength = float(input("poolLength: "))
poolWidth = float(input("poolWidth: "))
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
#the report about the customer's house
#Username
print("User Name:")
print(userName)
#Property Length
print("Property Length:")
print(propertyLength)
#Property Width
print("Property Width:")
print(propertyWidth)
#House Length
print("House Length:")
print(houseLength)
#House Width
print("House Width:")
print(houseWidth)
#Pool Length
print("Pool Length:")
print(poolLength)
#Pool Width
print("Pool Width:")
print(poolWidth)
#-------------------------------------------------
#In total
#Covered Spuare Footage
print("Covered Square Footage:")
print(coveredSquareFootage)
#Uncovered Square Footage
print("Uncovered Square Footage:")
print(uncoveredSquareFootage)
#----------------------------------------------------------
#End
print("Good bye!")
