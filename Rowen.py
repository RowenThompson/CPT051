print("Rowen Thompson")
print("CPT051")
print("Rowen.py")
print("October 2020")
print("------------------------")

CURRENCY = " Iron"
TAX = 0.01

Minecraft_Price = 200 
Minecraft_dungeons_Price = 400
Call_of_duty_warfare_Price = 100




print("What are you going to buy?")
print("Minecraft : " + str(Minecraft_Price) + CURRENCY)
print("Minecraft dungeons : " + str(Minecraft_dungeons_Price) + CURRENCY)
print("Call of duty warfare : " + str(Call_of_duty_warfare_Price) + CURRENCY)
print("Taxes not included")

def take_input():
    print("Enter your selection here")
    selection = input()
    return selection

menu_select = take_input()

print("You selected : " + menu_select)
print("First letter : " + menu_select)

