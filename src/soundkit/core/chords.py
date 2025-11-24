from typing import List, Dict
from .notes import midiKey, midiToNoteName, midiFreq
from ..exceptions import InvalidChordError, InvalidNoteError

CHORD_TYPES = {
    "maj": [0, 4, 7],
    "major": [0, 4, 7],
    "min": [0, 3, 7],
    "minor": [0, 3, 7],
    "dim": [0, 3, 6],
    "diminished": [0, 3, 6],
    "aug": [0, 4, 8],
    "augmented": [0, 4, 8],
    "7": [0, 4, 7, 10],
    "dominant7": [0, 4, 7, 10],
    "maj7": [0, 4, 7, 11],
    "major7": [0, 4, 7, 11],
    "min7": [0, 3, 7, 10],
    "minor7": [0, 3, 7, 10],
    "dim7": [0, 3, 6, 9],
    "diminished7": [0, 3, 6, 9],
    "half_dim7": [0, 3, 6, 10],
    "m7b5": [0, 3, 6, 10],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "9": [0, 4, 7, 10, 14],
    "maj9": [0, 4, 7, 11, 14],
}


def get_chord_notes(
    chord_root: str, chord_type: str = "maj", octave: int = 4, inversion: int = 0
) -> List[int]:
    """Get MIDI notes for common chords with optional inversion."""
    if chord_type not in CHORD_TYPES:
        raise InvalidChordError(f"Unknown chord type: {chord_type}")

    try:
        root_midi = midiKey(f"{chord_root}{octave}")
        intervals = CHORD_TYPES[chord_type]
        notes = [root_midi + interval for interval in intervals]

        # Apply inversion
        if inversion > 0:
            for _ in range(inversion):
                if notes:
                    note = notes.pop(0)
                    notes.append(note + 12)

        return notes
    except InvalidNoteError as e:
        raise InvalidChordError(f"Invalid chord root: {chord_root}") from e


def get_chord_frequencies(
    chord_root: str,
    chord_type: str = "maj",
    octave: int = 4,
    round_digits: int = 2,
    inversion: int = 0,
) -> List[float]:
    """Get frequencies for a chord."""
    midi_notes = get_chord_notes(chord_root, chord_type, octave, inversion)
    return [midiFreq(midiToNoteName(note), round_digits) for note in midi_notes]


def get_chord_names() -> List[str]:
    """Get list of available chord types."""
    return list(CHORD_TYPES.keys())
