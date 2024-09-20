import sys

# Define the Braille alphabet as a dictionary
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OO',
    'z': 'O..OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......'
}

# Braille capital and number indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'

# Reverse the dictionary to map Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}

def is_braille(s):
    return all(c in 'O. ' for c in s)

def braille_to_english(braille_string):
    braille_symbols = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    result = []
    capitalized = False
    numbers_mode = False
    
    for symbol in braille_symbols:
        if symbol == capital_indicator:
            capitalized = True
        elif symbol == number_indicator:
            numbers_mode = True
        else:
            char = english_alphabet.get(symbol, '')
            if char:
                if capitalized:
                    result.append(char.upper())
                    capitalized = False
                elif numbers_mode:
                    result.append(char)  # Treat as number
                elif char.isdigit():  # Check if the character is a digit
                    result.append(char)
                else:
                    result.append(char.lower())  # Convert to lowercase
            else:
                result.append('?')  # For unknown Braille symbols

            if char == ' ':
                numbers_mode = False
                capitalized = False  # Reset capitalized flag after a space

    return ''.join(result)

def english_to_braille(english_string):
    result = []
    for char in english_string:
        if char.isupper():
            result.append(capital_indicator)
            result.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            result.append(number_indicator)
            result.append(braille_alphabet[char])
        else:
            result.append(braille_alphabet.get(char.lower(), '......'))
    
    return ''.join(result)

def main():
    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == '__main__':
    main()
