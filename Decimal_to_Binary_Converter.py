# Start an infinite loop to keep the program running until the user chooses to exit
while True:
    try:
        # Prompt the user to choose an option
        menu = int(input("Choose an option: \n 1. Decimal to binary \n 2. Binary to decimal\n 3. Exit\n Option: "))
        
        # If the user chooses to exit, break the loop and end the program
        if menu == 3:
            print("Exiting...")
            break

        # Validate if the option is either 1 or 2
        if menu < 1 or menu > 2:
            raise ValueError("Invalid option. Please choose 1 or 2.")
        
        # Decimal to binary conversion
        if menu == 1:
            dec = int(input("Input your decimal number:\nDecimal: "))
            # Convert decimal to binary and remove the '0b' prefix
            print("Binary: {}".format(bin(dec)[2:]))
        
        # Binary to decimal conversion
        elif menu == 2:
            binary = input("Input your binary number:\n Binary: ")
            # Convert binary to decimal
            print("Decimal: {}".format(int(binary, 2)))
    
    except ValueError as e:
        # Handle invalid inputs and inform the user
        print("Error:", e)
        print("Please try again.")
