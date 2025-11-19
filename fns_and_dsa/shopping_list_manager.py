# shopping_list_manager.py


def display_menu():
    """Prints the main menu options to the console."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == "2":
            # 2. Remove Item
            if not shopping_list:
                print("The shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()

            # Use a try-except block to handle the case where the item is not found
            try:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                print(f"Error: '{item_to_remove}' not found in the list.")

        elif choice == "3":
            # 3. View List
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                # Loop through the list and print each item with its index (starting at 1)
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("--------------------------")

        elif choice == "4":
            # 4. Exit
            print("Goodbye! Your final list has been saved.")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
