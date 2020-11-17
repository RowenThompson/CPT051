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
    price = -1
    if(menu_select == 'A'):         #decision
        price = wizard_hat_price        #process
    elif(menu_select == 'B'):       #decision
        price = magic_sword_price       #process
    elif(menu_select == 'C'):       #decsion
        price = health_potion_price     #process
        
    price = price + (price * tax)   #process
    return price                    #end/return
     

#functions above
#------------------------------------Main-------------------------
#code below
author_sig() #Terminal/start

menu_select = 'F'
while(menu_select != 'Q'): #runwhile

    show_buy_menu() #output

    menu_select = take_input() #input


    while((menu_select != 'A') and  (menu_select != 'B') and (menu_select != 'C')): #decsion
        error_message()#output

        menu_select = take_input() #input  / Loop Control Variable Change
        
         
    print(calc_price(menu_select, TAX)) #process and output

#You have recieved a free gift! Randomly
    print("gift")
    print("end")#end
