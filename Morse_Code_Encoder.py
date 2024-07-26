def encode_morse(message):
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    string = ""
    for char in message:
        if char.upper() in char_to_dots:
            string += char_to_dots[char.upper()] + ' '
        else:
            string += '? '  # Placeholder for unknown characters
    return string.strip()

def decode_morse(morse_code):
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    dots_to_char = {v: k for k, v in char_to_dots.items()}

    message = ""
    words = morse_code.split(' / ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in dots_to_char:
                message += dots_to_char[char]
            else:
                message += '?'  # Placeholder for unknown characters
        message += ' '
    return message.strip()

def main():
    while True:
        choice = input("Choose an option: \n1. Encode a message\n2. Decode a message\n3. Exit\n")
        if choice == '1':
            message = input("Enter the message to encode: ")
            print("Encoded message in Morse code:")
            print(encode_morse(message))
        elif choice == '2':
            morse_code = input("Enter the Morse code to decode (use ' / ' to separate words): ")
            print("Decoded message:")
            print(decode_morse(morse_code))
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
