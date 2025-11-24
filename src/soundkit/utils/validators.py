import re
from typing import Union
from ..exceptions import InvalidNoteError, InvalidFrequencyError
from ..constants import MIDI_RANGE


def validate_note_name(note_name: str) -> bool:
    """Validate if a string is a properly formatted note name."""
    if not isinstance(note_name, str):
        return False

    pattern = r"^[CDEFGAB][B#]?-?\d+$"
    return bool(re.match(pattern, note_name.upper().replace(" ", "")))


def validate_midi_range(midi_number: int) -> bool:
    """Validate if a number is within the MIDI range."""
    return MIDI_RANGE[0] <= midi_number <= MIDI_RANGE[1]


def validate_frequency(frequency: float) -> bool:
    """Validate if a frequency is positive and reasonable."""
    return frequency > 0 and frequency <= 20000  # Human hearing range


def validate_octave(octave: int) -> bool:
    """Validate if an octave is within reasonable range."""
    return -1 <= octave <= 10


def normalize_note_name(note_name: str) -> str:
    """Convert various note formats to standard format."""
    if not isinstance(note_name, str):
        raise InvalidNoteError("Note name must be a string")

    note_name = note_name.upper().replace("-", "").replace(" ", "")
    note_name = note_name.replace("♭", "B").replace("♯", "#")
    return note_name
