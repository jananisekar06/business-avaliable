# MarketMate Business App

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        if quantity > self.stock:
            return False, "Insufficient stock!"
        self.stock -= quantity
        total = quantity * self.price
        return True, total


class MarketMate:
    def __init__(self):
        self.products = []
        self.total_sales = 0

    def add_product(self):
        name = input("Enter product name: ")
        try:
            price = float(input(f"Enter price for {name}: "))
            stock = int(input(f"Enter initial stock for {name}: "))
            product = Product(name, price, stock)
            self.products.append(product)
            print(f"Product '{name}' added successfully!")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    def view_products(self):
        if not self.products:
            print("\nNo products available.")
            return
        print("\nAvailable Products:")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product.name} - Price: ${product.price}, Stock: {product.stock}")

    def restock_product(self):
        self.view_products()
        try:
            choice = int(input("\nEnter the product number to restock: ")) - 1
            if choice < 0 or choice >= len(self.products):
                print("Invalid product selection!")
                return

            quantity = int(input(f"Enter the quantity to add to {self.products[choice].name}: "))
            self.products[choice].update_stock(quantity)
            print(f"Stock updated! {self.products[choice].name} now has {self.products[choice].stock} items.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    def sell_product(self):
        self.view_products()
        try:
            choice = int(input("\nEnter the product number to sell: ")) - 1
            if choice < 0 or choice >= len(self.products):
                print("Invalid product selection!")
                return

            quantity = int(input(f"Enter quantity to sell for {self.products[choice].name}: "))
            success, result = self.products[choice].sell(quantity)
            if success:
                self.total_sales += result
                print(f"Sale successful! Total sale amount: ${result}")
            else:
                print(result)
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    def view_sales_summary(self):
        print(f"\nTotal Sales Revenue: ${self.total_sales}")
        print("Remaining Stock:")
        self.view_products()

    def run(self):
        while True:
            print("\n--- MarketMate Business App ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Restock Product")
            print("4. Sell Product")
            print("5. View Sales Summary")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                self.restock_product()
            elif choice == "4":
                self.sell_product()
            elif choice == "5":
                self.view_sales_summary()
            elif choice == "6":
                print("Thank you for using MarketMate! Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# Main Execution
if __name__ == "__main__":
    app = MarketMate()
    app.run()
