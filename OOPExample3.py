class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"{self.product_id:<8}{self.name:<15}{self.price:<10.2f}{self.quantity:<10}{self.total_value():<12.2f}")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists")
            return
        self.products[product.product_id] = product
        print(f"Product '{product.name}' added to inventory")

    def update_stock(self, product_id, quantity_change):
        if product_id not in self.products:
            print("Product not found")
            return
        product = self.products[product_id]
        new_quantity = product.quantity + quantity_change
        if new_quantity < 0:
            print("Insufficient stock for this operation")
            return
        product.quantity = new_quantity
        print(f"Stock updated. {product.name} quantity = {product.quantity}")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed = self.products.pop(product_id)
            print(f"Removed '{removed.name}' from inventory")
        else:
            print("Product not found")

    def search_product(self, product_id):
        if product_id in self.products:
            self.products[product_id].display()
        else:
            print("Product not found")

    def low_stock_report(self, threshold):
        print(f"\nProducts with stock below {threshold}:")
        for product in self.products.values():
            if product.quantity < threshold:
                product.display()

    def display_all(self):
        print(f"\n{'ID':<8}{'Name':<15}{'Price':<10}{'Qty':<10}{'Value':<12}")
        print("-" * 55)
        for product in self.products.values():
            product.display()
        print("-" * 55)
        total = sum(product.total_value() for product in self.products.values())
        print(f"Total Inventory Value = {total:.2f}")


def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Product\n2. Update Stock\n3. Remove Product\n4. Search Product\n5. Low Stock Report\n6. Display All\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            inventory.add_product(Product(pid, name, price, quantity))
        elif choice == "2":
            pid = input("Enter product ID: ")
            change = int(input("Enter quantity change (positive to add, negative to remove): "))
            inventory.update_stock(pid, change)
        elif choice == "3":
            pid = input("Enter product ID to remove: ")
            inventory.remove_product(pid)
        elif choice == "4":
            pid = input("Enter product ID to search: ")
            inventory.search_product(pid)
        elif choice == "5":
            threshold = int(input("Enter stock threshold: "))
            inventory.low_stock_report(threshold)
        elif choice == "6":
            inventory.display_all()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()