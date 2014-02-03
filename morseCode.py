from RPi.GPIO import cleanup, setmode, setup, output, BOARD, OUT
from time import sleep

setmode(BOARD)
setup(7, OUT)

def on():
    output(7, True)
def off():
    output(7, False)
def blink(n=5, s=.5):
    for i in range(n):
        on()
        sleep(s)
        off()
        sleep(s)

To_Morse = dict({"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": "-....", "6": "--...", "7": "---..", "8": "----.", "9": "----.", "0": "-----"})

def getMorse(inputText):
    nuString = ""
    for i in inputText:
        if i == " ":
            nuString = nuString + To_Morse[i.upper()] + "|"
        else:
            nuString = nuString + " "
    return nuString


def parseOneZero(string):
    pass

def fromMorse(inputText):
    '''
        Translate Morse Code back into regular words
        1 = on
        0 = off
        eg. A = 10111000
            AN = 10111000111010
    '''
    collected = []
    toString = ""

    for i in inputText:
        if i == "1":
            #Do things
        else:
            #Else, i == 0

    #Check if pulse. Yes? 
        #Check if previous blip was a pulse
        #Yes? store it. Is the chunk a blip-trio? 
            #Yes? Dash
            #No? Dot
        #No? Then it is an off
            #If 1 space, end of blip sequence
            #If 3 spaces, end of letter
            #If 7 spaces, end of word
    pass


def dash(sp):
    on()
    on()
    on()
    off()

def dot(sp):
    on()
    off()

def letterSpace(sp):
    off()
    off()

def wordSpace(sp):
    off()
    off()
    off()
    off()

def toPulse(inputText):
    morse = getMorse(inputText)
    sp = 1
    for m in morse:
        if m == ".":
            dot(sp)
        elif m == "-":
            dash(sp)
        elif m == " ":
            wordSpace(sp)
        else:
            letterSpace(sp)
                