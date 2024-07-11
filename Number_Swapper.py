def num_swap():
    a = int(input("Enter the First Number:"))
    b = int(input("Enter the Second Number:"))
    print(f"Numbers Before Swapping:{a},{b}")
    c = a
    a = b
    b = c
    print(f"Numbers After Swapping:{a},{b}")

while True:
    num_swap()
    try_again = input("Do you want try again? (y/n):").lower()
    if try_again != "y":
        break
print("Thank You")
input("Press any key to exit....")
