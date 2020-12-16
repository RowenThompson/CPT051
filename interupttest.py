menu_select = ' '
auth_sig = 'Noelle Adkin'
buy_menu = 'A, B, C'
TAX = 0.01

shopping_list = []

shopping_list.append("Shopping List")

stock_items = ["Minecraft", "Cod", "Halo"]
stock_item_prices =[10.00, 20.00, 30.00]

def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

def error_message():
    print("This is an invalid selection.")

def calc_price(select, TAX):
    price = 0
    if(menu_select == 'A'):
        price = stock_item_prices[0]
        stock_item = stock_items[0]
        
    elif(menu_select == 'B'):
        price = Minecraft_dungeons_price
    elif(menu_select == 'C'):
        price = Call_of_duty_warfare_price

        
    price = price + (price * TAX)

    shopping_list.append(stock_item + str(price))
    return price

print(auth_sig)

while(menu_select != 'Q'):
    print("continue to")
    print(buy_menu)

    menu_select = take_input()

    while((menu_select != 'A') and  (menu_select != 'B') and (menu_select != 'C')  and (menu_select != 'I') and (menu_select != 'Z')): #decision
        if(menu_select == 'I'):
            continue
        if(menu_select == 'Z'):
            break
        error_message() #output

        menu_select = take_input() #input  / Loop Control Variable Change

    #print(calc_price(menu_select, TAX))
    #Print recipt
    for a in shopping_list:
        print(shopping_list.pop())
