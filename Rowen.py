def author_aig():
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
List_for_gaming = []
Shopping_cart = []

import random

Gifts_cool = ['Phone', '20 dollars', '100 amazon gift card', 'Giant zombie toy', 'Big Chicken toy', 'Big brain toy meme',]

def show_buy_menu():
    print("Buy menu")
    print("What are you going to buy?")
    print("A.)Minecraft : " + str(Minecraft_price) +  CURRENCY)
    print("B.)Minecraft dungeons : " + str(Minecraft_dungeons_price) +  CURRENCY)
    print("C.)Call of duty warfare : " + str(Call_of_duty_warfare_price) +  CURRENCY)
    print("Taxes not included")
    
def error_message():
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

author_aig()

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

#print("You got a gift!")
#print(random.choice(Gifts_cool))

if(menu_select == 'A'):
    List_for_gaming.append('A')
elif(menu_select == 'B'):
    List_for_gaming.append('B')
elif(menu_select == 'C'):
    List_for_gaming.append('C')

for item in List_for_gaming:
    if item == 'A':
        print("You want Minecraft?")
    elif item == 'B':
        print("You want Minecraft dungeons?")
    elif item == 'C':
        print("You want Call of duty warfare?")
print("Do you want to buy anything else?")
