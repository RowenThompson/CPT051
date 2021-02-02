#start
DISCOUNT_NAME_MEMBER = "Member"
DISCOUNT_NAME_SENIOR = "Senior"
DISCOUNT_NAME_NONE = "No Discount"
DISCOUNT_RATE_MEMBER = "0.15"
DISCOUNT_RATE_SENIOR = "0.15"
DISCOUNT_RATE_NONE = "0.15"
TAX_RATE = .075
print("Welcome to something")
userName = input("What is you're name? ")
itemName = input("What is the name of the item? ")
originalPrice = input("What is the Original Price: ")
howMany = input("How many? ")
menuSelection = input("What do you want to select? ")

if(menuSelection == 'a'):
    print("You selected a!")
    discountRate = DISCOUNT_RATE_MEMBER

elif(menuSelection == 'b'):
    print("You selected b!")
    
