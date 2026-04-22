# Function to import and call usermanager.py functions (register, login)
from utils.user_manager import UserManager
 
# Function to set object for calling out UserManager Functions
UM_i = UserManager()
 
# Main function to run the program
def main():
    while True:
        print("\nWelcome to the Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
 
        choice = input("\nEnter the number of your choice: ")
 
        if choice == "1":
            UM_i.register()
        elif choice == "2":
            UM_i.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()
