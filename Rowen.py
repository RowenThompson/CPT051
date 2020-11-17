def Author_aig():
    print("Rowen Thompson")
    print("CPT051")
    print("Rowen.py")
    print("October 2020")
    print("------------------------")

CURRENCY = "Iron"

TAX = 0.01

Minecraft_price = 200 
Minecraft_dungeons_price = 400
Call_of_duty_warfare_price = 100

def Show_Buy_menu():
    print("Buy menu")
    print("What are you going to buy?")
    print("A.)Minecraft :" + str(Minecraft_Price) + CURRENCY)
    print("B.)Minecraft dungeons :" + str(Minecraft_dungeons_Price) + CURRENCY)
    print("C.)Call of duty warfare :" + str(Call_of_duty_warfare_Price) + CURRENCY)
    print("Taxes not included")
    
def Error_message():
    print("This is an invalid selection.")

def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

def name_of_function():
    print("Code statment 1")
    print("Code statment 2")
    print("Code statment 3")

def calc_price(select, TAX):
    price = 0
    if(menu_select == 'A'):
        price = Minecraft_price
    elif(menu_select == 'B'):
        price = Minecraft_dungeons_price
    elif(menu_select == 'C'):
        price = Call_of_duty_warfare_price
    price = price + (price * TAX)
    return price

#Functions above
    #----------------------------------Main--------------------------------
#code below

+author_sig() #Terminal/start

show_buy_menu() #output

menu_select = take_input() #input

print("You selected : " + menu_select)
print("First letter : " + menu_select[0])

    
while((menu_select != 'A') and  (menu_select != 'B') and (menu_select != 'C')): #decision
    error_message() #output

    menu_select = take_input() #input  / Loop Control Variable Change

if(menu_select == 'A'):
    print("You selected A!")
elif(menu_select == 'B'):
    print("You selected B!")
elif(menu_select == 'C'):
    print("You selected C!")
   
print(calc_price(menu_select, TAX))
