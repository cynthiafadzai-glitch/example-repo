#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}\t{self.code}\t{self.product}\tR{self.cost:.2f}\t{self.quantity}"


#=============Shoe list===========

shoe_list = []


#==========Functions outside the class==============

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line/header

            for line in file:
                data = line.strip().split(",")

                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])

                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("The inventory.txt file could not be found.")

    except ValueError:
        print("There is invalid data in the inventory file.")

    except Exception as error:
        print("An error occurred:", error)


def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")

    try:
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        # Add the new shoe to the inventory file
        with open("inventory.txt", "a") as file:
            file.write(f"{country},{code},{product},{cost},{quantity}\n")

        print("Shoe successfully added.")

    except ValueError:
        print("Please enter a valid number for cost and quantity.")


def view_all():
    if len(shoe_list) == 0:
        print("There are no shoes in the inventory.")
        return

    print("\nCountry\t\tCode\t\tProduct\t\t\tCost\tQuantity")
    print("-" * 75)

    for shoe in shoe_list:
        print(shoe)


def re_stock():
    if len(shoe_list) == 0:
        print("There are no shoes in the inventory.")
        return

    # Find the shoe with the lowest quantity
    lowest = shoe_list[0]

    for shoe in shoe_list:
        if shoe.quantity < lowest.quantity:
            lowest = shoe

    print("\nShoe with the lowest quantity:")
    print(lowest)

    choice = input("Would you like to add stock to this shoe? (y/n): ").lower()

    if choice == "y":
        try:
            amount = int(input("How many shoes would you like to add? "))

            if amount <= 0:
                print("Please enter a quantity greater than 0.")
                return

            lowest.quantity += amount

            # Rewrite the inventory file with the updated quantity
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")

                for shoe in shoe_list:
                    file.write(
                        f"{shoe.country},{shoe.code},{shoe.product},"
                        f"{shoe.cost},{shoe.quantity}\n"
                    )

            print("Stock successfully updated.")
            print("New quantity:", lowest.quantity)

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("No stock was added.")


def search_shoe():
    code = input("Enter the shoe code you want to search for: ")

    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print("\nShoe found:")
            print(shoe)
            return

    print("Shoe not found.")


def value_per_item():
    if len(shoe_list) == 0:
        print("There are no shoes in the inventory.")
        return

    print("\nProduct\t\t\tValue")
    print("-" * 40)

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}\t\tR{value:.2f}")


def highest_qty():
    if len(shoe_list) == 0:
        print("There are no shoes in the inventory.")
        return

    highest = shoe_list[0]

    for shoe in shoe_list:
        if shoe.quantity > highest.quantity:
            highest = shoe

    print("\nShoe with the highest quantity:")
    print(highest)
    print("\nThis shoe is available for sale.")


#==========Main Menu=============

read_shoes_data()

while True:
    print("\n========== SHOE INVENTORY SYSTEM ==========")
    print("1. View all shoes")
    print("2. Add a new shoe")
    print("3. Restock shoe")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Find shoe with highest quantity")
    print("7. Exit")
    print("===========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Thank you for using the Shoe Inventory System.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 7.")