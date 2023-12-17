def display_menu():
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Delete item")
    print("3. View shopping list")
    print("4. Quit")


def shopping_cart():
    cart = []

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            cart.append(item)
            print(f"{item} added to the shopping cart.")

        elif choice == "2":
            if not cart:
                print("Your shopping cart is empty.")
            else:
                print("Current Shopping Cart:")
                for index, item in enumerate(cart, start=1):
                    print(f"{index}. {item}")

                item_to_remove = input("Enter the number of the item to delete: ")

                try:
                    index_to_remove = int(item_to_remove) - 1
                    removed_item = cart.pop(index_to_remove)
                    print(f"{removed_item} removed from the shopping cart.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid item number.")

        elif choice == "3":
            if not cart:
                print("Your shopping cart is empty.")
            else:
                print("Current Shopping Cart:")
                for index, item in enumerate(cart, start=1):
                    print(f"{index}. {item}")

        elif choice == "4":
            print("Items in your shopping cart upon quitting:")
            for item in cart:
                print(f"- {item}")
            print("Thank you for using the shopping cart. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the shopping cart program
shopping_cart()