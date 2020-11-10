def author_sig():
    print("Noelle Adkin")
    print("CPT051")
    print("noelle.py")
    print("October 2020")
    print("--------------------")

TAX = .01
CURRENCY = " Gold pieces"

wizard_hat_price = 100
magic_sword_price = 200
health_potion_price = 10

def show_buy_menu():
    print("What are you buying?")
    print("A.)" +"Wizard hat : " + str(wizard_hat_price) + CURRENCY)
    print("B.)" +"Magic Sword : " + str(magic_sword_price) + CURRENCY)
    print("C.)" +"Health Potion : " + str(health_potion_price) + CURRENCY)
    print("* Taxes not included")

def take_input():
    print("Enter your Selection here:")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

def error_message():
    print("This is an invalid selection.")

def name_of_function():
    print("Code statment 1")
    print("Code statment 2")

    print("code statment 3")

def calc_price(select, tax):
    price = 0
    if(menu_select == 'A'):
        price = wizard_hat_price
    elif(menu_select == 'B'):
        price = magic_sword_price
    elif(menu_select == 'C'):
        price = health_potion_price
    price = price + (price * tax)
    return price
    

#functions above
#------------------------------------Main-------------------------
#code below
author_sig() #Terminal/start

show_buy_menu() #output

menu_select = take_input() #input


while((menu_select != 'A') and  (menu_select != 'B') and (menu_select != 'C')): 
    error_message()

    menu_select = take_input() #input  / Loop Control Variable Change

if(menu_select == 'A'):
    print("You selected A!")
elif(menu_select == 'B'):
    print("You selected B!")
elif(menu_select == 'C'):
    print("You selected C!")
   
print(calc_price(menu_select, TAX))
