MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().upper()
    # Each word should be on its own line (words separated by space in original)
    text = text.replace(' ', '\n')  
    # Create a translation table from single characters to Morse strings
    table = str.maketrans({k: v  for k, v in MORSE_CODE.items()})

    # Translate the text
    morse_text = text.translate(table)

    # Each word should be on its own line (words separated by space in original)
    #morse_text = morse_text.replace('  ', '\n')  # double space = original space between words

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(morse_text.strip())
    return morse_text.strip()

#run the function to create the output file
if __name__ == "__main__":
    english_to_morse()
    print("Morse code translation complete. Check the output file.")
