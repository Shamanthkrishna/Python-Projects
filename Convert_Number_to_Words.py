# Dictionaries to map digits and numbers to their word equivalents
one_digit_words = {
    '0': ["zero"],
    '1': ["one"],
    '2': ["two", "twen"],
    '3': ["three", "thir"],
    '4': ["four", "for"],
    '5': ["five", "fif"],
    '6': ["six"],
    '7': ["seven"],
    '8': ["eight"],
    '9': ["nine"],
}

# Lists for special two-digit numbers and tens
two_digit_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# Constants for large number terms and hundred
hundred = "hundred"
large_sum_words = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

def number_to_words(num):
    """Convert a number represented as a string to its English words equivalent."""
    # Special case for zero
    if num == '0':
        return one_digit_words['0'][0]
    
    # Ensure the number has groups of three digits
    if len(num) % 3 != 0:
        num = num.zfill(3 * (((len(num) - 1) // 3) + 1))

    # Split the number into chunks of three digits
    chunks = [num[i:i + 3] for i in range(0, len(num), 3)]
    words = []

    for i, chunk in enumerate(chunks):
        if chunk == '000':
            continue  # Skip chunk if all digits are zero
        
        # Handle hundreds place
        if len(chunk) == 3:
            hundreds, remainder = chunk[0], chunk[1:]
            if hundreds != '0':
                words.append(one_digit_words[hundreds][0] + " " + hundred)
            chunk = remainder
        
        # Handle two-digit numbers
        if len(chunk) == 2:
            if chunk.startswith('1'):
                words.append(two_digit_words[int(chunk[1])])
            else:
                tens, ones = chunk
                if ones != '0':
                    words.append(tens_words[int(tens)] + " " + one_digit_words[ones][0])
                else:
                    words.append(tens_words[int(tens)])
        
        # Handle single-digit numbers
        if len(chunk) == 1 and chunk != '0':
            words.append(one_digit_words[chunk][0])
        
        # Append large number terms (thousand, million, etc.)
        if i < len(chunks) - 1:
            words.append(large_sum_words[len(chunks) - 2 - i])
    
    # Join all words and format the final result
    return " ".join(words).replace("  ", " ").strip().capitalize()

def main():
    """Main function to handle user input and output."""
    while True:
        try:
            n = input("Enter any number to convert it into words or 'exit' to stop: ")
            if n.lower() == "exit":
                break
            if not n.isdigit():
                raise ValueError  # Handle non-digit inputs
            print(n, "-->", number_to_words(n))  # Convert and display result
        except ValueError:
            print("Error: Invalid number! Please enter a valid integer.")

if __name__ == "__main__":
    main()  # Execute the main function
