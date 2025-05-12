# Interactive Inventory Management System with Preloaded Products

# Dictionary to store inventory data (product name, price, quantity)
inventory = {
    "Laptop": {"price": 1500, "quantity": 5},
    "Phone": {"price": 800, "quantity": 10},
    "Tablet": {"price": 600, "quantity": 8},
    "Headphones": {"price": 200, "quantity": 15},
    "Mouse": {"price": 50, "quantity": 20}
}

def add_product():
    """Allows the user to add a new product to the inventory."""
    product_name = input("Enter the product name: ")
    if product_name in inventory:
        print("Error: The product already exists in the inventory.")
        return
    try:
        product_price = float(input("Enter the product price: "))
        product_quantity = int(input("Enter the available quantity: "))
        if product_price < 0 or product_quantity < 0:
            print("Error: Price or quantity cannot be negative.")
            return
        inventory[product_name] = {"price": product_price, "quantity": product_quantity}
        print(f"Product '{product_name}' added successfully.")
    except ValueError:
        print("Error: Please enter valid numerical values.")

def view_product():
    """Allows the user to search for a product and display its details."""
    product_name = input("Enter the product name to view details: ")
    if product_name in inventory:
        print(f"Name: {product_name}, Price: {inventory[product_name]['price']}, Quantity: {inventory[product_name]['quantity']}")
    else:
        print("Error: Product not found.")

def update_price():
    """Allows the user to update the price of an existing product."""
    product_name = input("Enter the product name to update price: ")
    if product_name in inventory:
        try:
            new_price = float(input("Enter the new price: "))
            if new_price < 0:
                print("Error: Price cannot be negative.")
                return
            inventory[product_name]['price'] = new_price
            print(f"Price of '{product_name}' updated to {new_price}.")
        except ValueError:
            print("Error: Please enter a valid numeric price.")
    else:
        print("Error: Product not found.")

def remove_product():
    """Allows the user to remove a product from the inventory."""
    product_name = input("Enter the product name to remove: ")
    if product_name in inventory:
        del inventory[product_name]
        print(f"Product '{product_name}' removed successfully.")
    else:
        print("Error: Product not found.")

def calculate_total_value():
    """Calculates and displays the total value of all products in the inventory."""
    total_value = sum(inventory[product]["price"] * inventory[product]["quantity"] for product in inventory)
    print(f"The total value of the inventory is: {total_value}")

def display_inventory():
    """Displays the complete inventory with product details."""
    print("\nCurrent Inventory:")
    for product_name, details in inventory.items():
        print(f"- {product_name}: Price ${details['price']}, Quantity {details['quantity']}")

def menu():
    """Displays the menu options and allows user interaction."""
    while True:
        print("\nInventory Management Menu")
        print("1. Add a Product")
        print("2. View a Product")
        print("3. Update Product Price")
        print("4. Remove a Product")
        print("5. Calculate Total Inventory Value")
        print("6. Display All Inventory")
        print("7. Exit")
        
        option = input("Select an option: ")
        
        if option == "1":
            add_product()
        elif option == "2":
            view_product()
        elif option == "3":
            update_price()
        elif option == "4":
            remove_product()
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            display_inventory()
        elif option == "7":
            print("Exiting the system...")
            break
        else:
            print("Invalid option, please try again.")

# Start the interactive menu with preloaded inventory
menu()