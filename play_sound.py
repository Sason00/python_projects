import winsound


"""
Beep(frequency, duration)
    A wrapper around the Windows Beep API.

    frequency
      Frequency of the sound in hertz.
      Must be in the range 37 through 32,767.
    duration
      How long the sound should play, in milliseconds.
"""


ONE_AND_A_HALF = 1500
WHOLE = 1000
THREE_QUARTERS = 750
HALF = 500
THREE_HEIGHT = 375
QUARTER = 250
THREE_SIXTEEN = 1875
EIGHTH = 125

NOTES = {
    "D#1": 38,
    "E1": 41,
    "F1": 43,
    "F#1": 46,
    "G1": 48,
    "G#1": 51,
    "A1": 55,
    "A#1": 58,
    "B1": 61,
    "C2": 65,
    "C#2": 69,
    "D2": 73,
    "D#2": 77,
    "E2": 82,
    "F2": 87,
    "F#2": 92,
    "G2": 97,
    "G#2": 103,
    "A2": 110,
    "A#2": 116,
    "B2": 123,
    "C3": 130,
    "C#3": 138,
    "D3": 146,
    "D#3": 155,
    "E3": 164,
    "F3": 174,
    "F#3": 184,
    "G3": 195,
    "G#3": 207,
    "A3": 220,
    "A#3": 233,
    "B3": 246,
    "C4": 261,
    "C#4": 277,
    "D4": 293,
    "D#4": 311,
    "E4": 329,
    "F4": 349,
    "F#4": 369,
    "G4": 391,
    "G#4": 415,
    "A4": 440,
    "A#4": 466,
    "B4": 493,
    "C5": 523,
    "C#5": 554,
    "D5": 587,
    "D#5": 622,
    "E5": 659,
    "F5": 698,
    "F#5": 739,
    "G5": 783,
    "G#5": 830,
    "A5": 880,
    "A#5": 932,
    "B5": 987,
    "C6": 1046,
    "C#6": 1108,
    "D6": 1174,
    "D#6": 1244,
    "E6": 1318,
    "F6": 1396,
    "F#6": 1479,
    "G6": 1567,
    "G#6": 1661,
    "A6": 1760,
    "A#6": 1864,
    "C7": 2093,
    "C#7": 2217,
    "D7": 2349,
    "D#7": 2489,
    "E7": 2637,
    "F7": 2793,
    "F#7": 2959,
    "G7": 3135,
    "G#7": 3322,
    "A7": 3520,
    "A#7": 3729,
    "B7": 3951,
    "C8": 4186,
    "C#8": 4434,
    "D8": 4698,
    "D#8": 4978,
    "E8": 5274,
    "F8": 5587,
    "F#8": 5919,
    "G8": 6271,
    "G#8": 6644,
    "A8": 7040,
    "A#8": 7458,
    "B8": 7902,
    "C9": 8372,
    "C#9": 8869,
    "D9": 9397,
    "D#9": 9956,
    "E9": 10548,
    "F9": 11175,
    "F#9": 11839,
    "G9": 12543,
    "G#9": 13289,
    "A9": 14080,
    "A#9": 14917,
    "B9": 15804,
}

"""
for i in NOTES.keys():
    winsound.Beep(NOTES[i], EIGHTH)
"""

winsound.Beep(NOTES["B2"], WHOLE)
winsound.Beep(NOTES["D2"], WHOLE)
winsound.Beep(NOTES["E2"], WHOLE)
winsound.Beep(NOTES["C#2"], WHOLE)
winsound.Beep(NOTES["A2"], WHOLE)
winsound.Beep(NOTES["E2"], WHOLE)
winsound.Beep(NOTES["C#2"], WHOLE)
winsound.Beep(NOTES["F#2"], WHOLE)
winsound.Beep(NOTES["D2"], WHOLE)
