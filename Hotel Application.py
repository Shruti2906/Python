starter = ["papad", "soup"]
starterPrice = [30, 50]

vegMenu = ["Dal-Khichadi", "Pav-bhaji  ", "Misal      ", "Dosa       "]
vegMenuPrice = [80, 90, 150, 200]

nonvegMenu = ["Biryani", "Chiken Role"]
nonvegMenuPrice = [200, 250]

order = []

price = 0.0;

while True:
    print("\n********************* Menu ************************")

    print("\n1 : Starters\n2 : Veg Menu\n3 : NonVeg Menu")
    ch = int(input("Enter your choice .."))
    if ch == 1:
        while True:
            for x in range(len(starter)):
                print(starter[x],"\t",starterPrice[x])
            val = int(input("Enter Your Order : "))
            if(val <= len(starter)):
                order.append([starter[val-1],starterPrice[val-1]])
                price += starterPrice[val-1];
            else:
                print("The Menu is not availble..")
            sch = int(input("Want To Order more from Starter press 1 : "))
            if sch != 1:
                break;

    if ch == 2:
        while True:
            for x in range(len(vegMenu)):
                print(vegMenu[x], "\t", vegMenuPrice[x])
            val = int(input("Enter Your Order : "))
            if (val <= len(vegMenu)):
                order.append([vegMenu[val - 1], vegMenuPrice[val - 1]])
                price += vegMenuPrice[val - 1];
            else:
                print("The Menu is not availble..")
            sch = int(input("Want To Order more from Veg Menu press 1 : "))
            if sch != 1:
                break;

    if ch == 3:
        while True:
            for x in range(len(nonvegMenu)):
                print(nonvegMenu[x], "\t", nonvegMenuPrice[x])
            val = int(input("Enter Your Order : "))
            if (val <= len(vegMenu)):
                order.append([nonvegMenu[val - 1], nonvegMenuPrice[val - 1]])
                price += nonvegMenuPrice[val - 1];
            else:
                print("The Menu is not availble..")
            sch = int(input("Want To Order more from Veg Menu press 1 : "))
            if sch != 1:
                break;

    mch = int(input("Want To see Menu Again press 1 : "))
    if mch != 1:
        break;


#print(order)
print("===================== Your Order =====================")
i = 0
for i in order:
    print("")
    for x in i:
        print(x,end=" ")
print("\nYour Bill\t:\t",price)