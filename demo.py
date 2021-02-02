menu_select = 'q'
price = 1
discount_rate = 0.05



if(menu_select == 'a'):
    print("a")
elif(menu_select == 'b'):
    print("b")
else:
    print("c or other")

if(price > 0):
    print("Recepit")
    print(str((discount_rate * 100)) + "%" )
