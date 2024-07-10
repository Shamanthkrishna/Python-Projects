def acronym_gen():
    user_input = str(input("Enter a Phrase: "))

    text = user_input.split()

    a = " "

    for i in text:
        a = a+str(i[0]).upper()

    print(a)

while True:
    acronym_gen()
    try_again = input("Do you want to try again? (y/n):").lower()
    if try_again != "y":
        break
print("Thank You")