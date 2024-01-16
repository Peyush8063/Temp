import os

class Cars:
    def __init__(self):
        self.Company = ["Maruti", "Honda", "Toyota", "Ford", "Tata", "Mahindra", "Hyundai", "Renault", "Skoda", "Volkswagen", "Mercedes", "BMW", "Audi"]
        self.Model = ["Swift", "City", "Innova", "Figo", "Nano", "XUV", "i20", "Kwid", "Octavia", "Polo", "Benz", "X5", "A4"]
        self.Color = ["Red", "White", "Black", "Blue", "Silver", "Yellow", "Green", "Grey", "Brown", "Orange", "Purple", "Pink", "Gold"]
        self.MaxSpeed = ["180", "200", "210", "190", "160", "170", "180", "190", "200", "210", "220", "230", "240"]
        self.FuelType = ["Petrol", "Diesel", "Petrol", "Diesel", "Petrol", "Diesel", "Petrol", "Diesel", "Petrol", "Diesel", "Petrol", "Diesel", "Petrol"]
        self.Manufacturer = ["India", "Japan", "India", "India", "Japan", "India", "Japan", "France", "India", "Germany", "India", "Germany", "Germany"]
        self.Price = [500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000]

class LeaseInfo:
    def __init__(self):
        self.First_Name = []
        self.Last_Name = []
        self.National_ID = []
        self.Phone_Number = []
        self.Payment = []

def menu():
    num = 1
    for i in range(13):
        print(f"\t\t\t\t{num}. {car.Company[i]}")
        num += 1

def details(choice):
    j = choice - 1
    print("\t\t\t ----------------------------")
    print(f"\t\t\t Company: {car.Company[j]}")
    print("\t\t\t ----------------------------")
    print(f"\t\t\t Model: {car.Model[j]}")
    print(f"\t\t\t Color: {car.Color[j]}")
    print(f"\t\t\t Max Speed: {car.MaxSpeed[j]}")
    print(f"\t\t\t Fuel Type: {car.FuelType[j]}")
    print(f"\t\t\t Manufacturer: {car.Manufacturer[j]}")
    print("\n\t\t\t ----------------------------")
    print(f"\t\t\t Price: {car.Price[j]}")
    print("\t\t\t ----------------------------")

def check_lease(j):
    if lease.Payment[j] >= car.Price[j]:
        print("\t\t\t Payment Successful")
        print("\t\t\t Thank you for using our service")
    else:
        print("\t\t\t Payment Unsuccessful")
        print(f"\t\t\t Please pay the full amount {car.Price[j]}")
        print("\t\t\t--------------------------------------------")
        lease.Payment[j] = int(input("\t\t\t Enter the amount you are paying : "))
        print("\t\t\t--------------------------------------------")
        check_lease(j)

def user_input(choice):
    i = 0
    j = choice - 1
    print("\t\t\t--------------------------------------------")
    print("\t\t\t\t Please Provide your details : ")
    print("\t\t\t--------------------------------------------")

    print("\t Note : PAYMENT WON'T BE PROCEEDED IF THE AMOUNT IS LESS THAN THE RATE OF THE CAR ")
    print("\t\t\t--------------------------------------------")
    lease.First_Name.append(input("\t\t\t First Name : "))
    lease.Last_Name.append(input("\t\t\t Last Name : "))
    lease.National_ID.append(input("\t\t\t Enter your National ID : "))
    lease.Phone_Number.append(input("\t\t\t Enter your Phone Number : "))
    print("\t\t\t--------------------------------------------")
    lease.Payment.append(int(input("\t\t\t Enter the amount you are paying : ")))
    print("\t\t\t--------------------------------------------")
 # Ensure the length of lease.Payment is greater than j before calling check_lease
    while len(lease.Payment) <= j:
        lease.Payment.append(0)

    check_lease(j)

def login():
    password = ""
    print("\t\t\t\t Car Rental System login")
    print("\t\t\t -------------------------------------------")
    password_input = input("\t\t\t Enter Password: ")

    if password_input == "pass":
        print("\t\t\t Password Matched")
        print("\t\t\t Loading...")
        os.system("PAUSE")
        print("\t\t\t Access Granted! Welcome to our system")
        print("\t\t\t Developed by: Amogh Saxena")
        os.system("cls")
    else:
        print("\t\t\t Password Not Matched")
        print("\t\t\t Try Again")
        os.system("PAUSE")
        os.system("cls")
        login()

def main():
    login()
    decide = "yes"
    print("\t\t\t--------------------------------------------")
    print("\t\t\t\t Welcome to Car Rental System")
    print("\t\t\t--------------------------------------------")
    print("\n\t\t\t Choose your option")
    print("\t\t\t--------------------------------------------")

    while decide != "exit":
        menu()
        print("\t\t\t--------------------------------------------")
        choice = int(input("\t\t\t Your Choice: "))
        os.system("cls")
        details(choice)

        decide = input("\t\t\t Are you sure you want to rent this car (yes/no/exit) : ")

        if decide.lower() == "yes":
            user_input(choice)
            print("\t\t\t Do you want to continue (yes/no)")
            decide = input()

            if decide.lower() == "no":
                print("\t\t\t Thank you for using our system")
                break
            os.system("cls")
        elif decide.lower() == "exit":
            print("\t\t\t Thank you for using our system")
            break
        else:
            if decide.lower() == "no":
                os.system("cls")
                continue

if __name__ == "__main__":
    car = Cars()
    lease = LeaseInfo()
    main()
