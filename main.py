import datetime
import random

# Global Menu Items (You can add them from the previous example)
menu_items = [
    {'id': 1, 'name': 'Idli', 'price': 40},
    {'id': 2, 'name': 'Dosa', 'price': 50},
    {'id': 3, 'name': 'Poha', 'price': 30},
    {'id': 4, 'name': 'Upma', 'price': 35},
    {'id': 5, 'name': 'Vada', 'price': 20},
    {'id': 6, 'name': 'Samosa', 'price': 15},
    {'id': 7, 'name': 'Aloo Paratha', 'price': 40},
    {'id': 8, 'name': 'Chai', 'price': 10},
    {'id': 9, 'name': 'Coffee', 'price': 15},
    {'id': 10, 'name': 'Paneer Paratha', 'price': 45},
    {'id': 11, 'name': 'Uttapam', 'price': 55},
    {'id': 12, 'name': 'Sabudana Khichdi', 'price': 40},
    {'id': 13, 'name': 'Besan Chilla', 'price': 30},
    {'id': 14, 'name': 'Dhokla', 'price': 25},
    {'id': 15, 'name': 'Bhature', 'price': 20},
    {'id': 16, 'name': 'Poori Bhaji', 'price': 45},
    {'id': 17, 'name': 'Masala Dosa', 'price': 30},
    {'id': 18, 'name': 'Fruit Salad', 'price': 35},
    {'id': 19, 'name': 'Mango Lassi', 'price': 20},
    {'id': 20, 'name': 'Fresh Juice', 'price': 25},
]

# Step 1: Display Static Menu
def display_menu():
    print("----- Welcome to XYZ Restaurant -----")
    for i in range(0, len(menu_items), 2):
        item1 = menu_items[i]
        item2 = menu_items[i + 1] if i + 1 < len(menu_items) else {'id': '', 'name': '', 'price': ''}
        print(f"{item1['id']:<3} {item1['name']:<12} {item1['price']:<5} || "
              f"{item2['id']:<3} {item2['name']:<12} {item2['price']:<5}")
    
    print("0. Exit")

# Step 2: Take Order
def take_order():
    order = []
    while True:
        choice = int(input("Enter the item ID to add to your order (0 to finish): "))
        if choice == 0:
            break
        quantity = int(input(f"Enter the quantity of the selected item: "))
        if choice <= len(menu_items) and choice >= 1:
            item = {
                'item': menu_items[choice - 1]['name'],
                'qty': quantity,
                'price': menu_items[choice - 1]['price']
            }
            order.append(item)
        else:
            print("Invalid choice. Please try again.")
    return order

# Step 3: Calculate Total Bill
def calculate_total(order):
    return sum(item['price'] * item['qty'] for item in order)

# Step 4: Print Bill
def print_bill(order, total):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_number = random.randint(1000, 9999)
    
    print("------------------------------------------------")
    print("                  XYZ Restaurant")
    print("------------------------------------------------")
    print(f"Order Number: {order_number:<28}")
    print(f"Date and Time: {current_time:<24}")
    print("------------------------------------------------")
    print(f"{'Item':<18} {'Quantity':<8} {'Price':<8}")
    print("------------------------------------------------")
    for item in order:
        print(f"{item['item']:<18} {item['qty']:<8} Rs. {item['price'] * item['qty']:<8}")
    print("------------------------------------------------")
    print(f"{'Total:':<28} Rs. {total:<8}")
    print("------------------------------------------------")
    print("          Thank you for dining with us!")
    print("------------------------------------------------")

# Main Program
if __name__ == "__main__":
    display_menu()
    order = take_order()
    total = calculate_total(order)
    print_bill(order, total)
