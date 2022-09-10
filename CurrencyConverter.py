
print("\n------------------ Currency Convertor ------------------\n")
amt = float(input("Enter Amount in INR : "))
choice = int(input("1] United States Dollar\t\t2] Russian Ruble\t3] Pound sterling\t:\t"))

if choice == 1:
    converted = amt*79.85;
    print("United States Dollar",converted)
elif choice == 2:
    converted = amt * 1.34;
    print("Russian Ruble", converted)
elif choice == 3:
    converted = amt * 94.34;
    print("Pound sterling", converted)
else:
    print("Invalid choice")