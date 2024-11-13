from bll.classes.api.interaction import interact_with_user

def display_menu():
    while True:
        print("\nOptions:")
        print("1. Get data")
        print("2. Display history")
        print("3. Save data")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            interact_with_user('get')
        elif choice == '2':
            interact_with_user('history')
        elif choice == '3':
            interact_with_user('save')
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
