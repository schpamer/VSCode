MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4',
'.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X',
'.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I',
'..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U',
'..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6',
'-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
'....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
'-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
'--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C',
'---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$',
'.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(',
'---..': '8', '...--': '3'}

def decodeMorse(morseCode):
    MORSE_CODE['@'] = ' '
    morseCode = morseCode.strip().replace('  ',' @ ')
    return ''.join([MORSE_CODE[code] for code in morseCode.split()])

p = decodeMorse('.... . -.--   .--- ..- -.. .')
print(p)

#  morseAlphabet ={
#         "A" : ".-",
#         "B" : "-...",
#         "C" : "-.-.",
#         "D" : "-..",
#         "E" : ".",
#         "F" : "..-.",
#         "G" : "--.",
#         "H" : "....",
#         "I" : "..",
#         "J" : ".---",
#         "K" : "-.-",
#         "L" : ".-..",
#         "M" : "--",
#         "N" : "-.",
#         "O" : "---",
#         "P" : ".--.",
#         "Q" : "--.-",
#         "R" : ".-.",
#         "S" : "...",
#         "T" : "-",
#         "U" : "..-",
#         "V" : "...-",
#         "W" : ".--",
#         "X" : "-..-",
#         "Y" : "-.--",
#         "Z" : "--..",
#         " " : "/"
#         }

#     inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())


#     testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "

#     # parse a morse code string positionInString is the starting point for decoding
#     def decodeMorse(code, positionInString = 0):
        
#         if positionInString < len(code):
#             morseLetter = ""
#             for key,char in enumerate(code[positionInString:]):
#                 if char == " ":
#                     positionInString = key + positionInString + 1
#                     letter = inverseMorseAlphabet[morseLetter]
#                     return letter + decodeMorse(code, positionInString)
                
#                 else:
#                     morseLetter += char
#         else:
#             return ""
        
#     #encode a message in morse code, spaces between words are represented by '/'
#     def encodeToMorse(message):
#         encodedMessage = ""
#         for char in message[:]:
#             encodedMessage += morseAlphabet[char.upper()] + " "
                
#         return encodedMessage