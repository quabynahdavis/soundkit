# Standard tuning frequencies
CONCERT_PITCH: int = 440  # Key A
MIDI_RANGE: tuple[int, int] = (0, 127)

# Common frequencies for reference
REFERENCE_FREQUENCIES: dict[str, float] = {
    "C0": 16.35,
    "C#0": 17.32,
    "D0": 18.35,
    "D#0": 19.45,
    "E0": 20.60,
    "F0": 21.83,
    "F#0": 23.12,
    "G0": 24.50,
    "G#0": 25.96,
    "A0": 27.50,
    "A#0": 29.14,
    "B0": 30.87,
    "C4": 261.63,
    "A4": 440.00,
    "C5": 523.25,
}

# Standard note names
NOTE_NAMES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_NAMES_FLAT = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
FLAT_TO_SHARP: dict[str, str] = {
    "DB": "C#",
    "EB": "D#",
    "FB": "E",
    "GB": "F#",
    "AB": "G#",
    "BB": "A#",
    "CB": "B",
}
