
# Morse code dictionary containing key: values pairs like text:morse
morse_code = {

    # alphabets
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..',

    # numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    # symbols
    ',': ',', '?': '?', '!': '!', ':': ':', ';': ';',
    "'": "'", '"': '"', '(': '(', ')': ')',
    '&': '&', '=': '=', '+': '+', '_': '_', '@': '@', '$': '$',
    '%': '%', '[': '[', ']': ']', '{': '{', '}': '}', '<': '<',
    '>': '>', '^': '^', '#': '#', '*': '*', '|': '|',
    '~': '~', '`': '`', '¿': '¿', '¡': '¡', ' ': '/',

    # for morse to text
    '/': ' '
}

# Input String (text) to convert into morse
text = input("Type anything : ").lower()

# converting every character in the text into morse using values from morse_code dictionary (is a list)
morse= []
for char in text:
    try:
        morse.append(morse_code[char])
    except KeyError:
        pass

# Joining the list for displaying the morse code
display_morse = ' '.join(morse)
print(f"Morse : {display_morse}")

input_morse = input("Want to convert morse into text? Enter the morse code:\n")
input_morse = input_morse.split(' ')
# Converting morse code back to text
new_text = ''
for char in input_morse:
    for key in morse_code:
        if char == morse_code[key]:
            new_text += key

# Displaying the converted text
print(f"Text : {new_text}")
