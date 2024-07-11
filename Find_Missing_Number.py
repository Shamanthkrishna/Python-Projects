
def get_user_numbers():
    user_input = input("Enter a sequence of numbers separated by commas: ")
    numbers = list(map(int, user_input.split(',')))
    return numbers

def findMissingNumber(n):
    numbers = set(n)
    output = []

    for i in range(1, n[-1]+1):
        if i not in numbers:
            output.append(i)
    return output

while True:
        list_of_numbers = get_user_numbers()
        print(f"Input numbers: {list_of_numbers}")

        missing_numbers = findMissingNumber(list_of_numbers)
        print(f"Missing numbers: {missing_numbers}")

        combined_list = sorted(list_of_numbers + missing_numbers)
        print(f"Combined list: {combined_list}")

        try_again = input("Do you want try again? (y/n):").lower()
        if try_again != "y":
            break

print("Thank You")
input("Press any key to exit....")