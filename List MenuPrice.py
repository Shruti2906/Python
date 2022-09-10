
name = ["Pavbhaji   ", "Puri-Bhaji", "Pasta     ", "Sandwitch"]
price = [80 , 100, 200, 150]

order = []
sum = 0

ch = "y"
i = 0
while((ch == "y") or (ch=="yes")):

    for i in range(0, len(name)):
        print((i+1)," : ",name[i],"\t\t\t",":\t\t\t",price[i])

    val = int(input("Enter Your Favorite dish : "))
    if val>=1 and val<5:
        order.append(val-1)
        sum = sum+price[val-1]
    else:
        print('dish is not available..')

    ch = input("Do you want to order more(Y/N) : ")

print("================= your Bill ==================")
for x in order:
    print(name[x])

print("Total Bill :",sum)

print("thank you..")