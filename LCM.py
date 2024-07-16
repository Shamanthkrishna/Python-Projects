import math

def least_common_multiple(a, b):
    greater = max(a, b)
    lcm = greater
    
    while True:
        if (lcm % a == 0) and (lcm % b == 0):
            break
        lcm += greater  # Increment by the larger number to optimize
        
    return lcm

# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the least common multiple
result = least_common_multiple(num1, num2)
print(f"The least common multiple of {num1} and {num2} is: {result}")
