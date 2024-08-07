from connector import *
from phonebook import *



def main():
    create_table()
    while True:
        print("\n☎️  PHONE-BOOK")
        print("1. Add Contact")
        print("2. View Contact Details")
        print("3. Load Contacts to CSV")
        print("4. Import Contacts to PhoneBook from CSV")
        print("5. Exit")

        choice = int(input("\nEnter your Choice: "))

        if choice==1:
            add_contact()
        elif choice==2:
            view_contact()
        elif choice==3:
            load_to_csv()
        elif choice==4:
            import_from_csv()
        elif choice==5:
            print("Exiting....")
            break
        else:
            print("Invalid Input, Try Again")
    
if __name__ == "__main__":
    main()