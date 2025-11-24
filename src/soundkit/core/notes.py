import re
import math
from typing import List, Union
from ..exceptions import InvalidNoteError, InvalidOctaveError, InvalidFrequencyError
from ..constants import CONCERT_PITCH, NOTE_NAMES_SHARP, NOTE_NAMES_FLAT, FLAT_TO_SHARP
from ..utils.validators import normalize_note_name

def normalize_note_name(note_name: str) -> str:
    """Convert various note formats to standard format."""
    if not isinstance(note_name, str):
        raise InvalidNoteError("Note name must be a string")
    note_name = (
        note_name.upper()
        .replace("-", "")
        .replace(" ", "")
        .replace("♭", "B")
        .replace("♯", "#")
    )
    return note_name


def midiKey(note_name: str) -> int:
    """Convert note name to MIDI note number"""
    note_map = {
        "C": 0,
        "C#": 1,
        "DB": 1,
        "D": 2,
        "D#": 3,
        "EB": 3,
        "E": 4,
        "FB": 4,
        "F": 5,
        "F#": 6,
        "GB": 6,
        "G": 7,
        "G#": 8,
        "AB": 8,
        "A": 9,
        "A#": 10,
        "BB": 10,
        "B": 11,
        "CB": 11,
    }
    try:
        note_name = normalize_note_name(note_name)
        pattern = r"^([CDEFGAB][B#]?)(-?\d+)$"
        match = re.match(pattern, note_name)
        
        if not match: raise InvalidNoteError(f"Invalid note name format: {note_name}")
        
        note = match.group(1).upper()
        if len(note) ==2 and note[1]=='B': note = FLAT_TO_SHARP.get(note, note)
        
        octave = int(match.group(2))
        if octave < -1 or octave > 10:
            raise InvalidOctaveError(f"Octave out of range (-1 to 10): {octave}")

        if note not in note_map:
            raise InvalidNoteError(f"Note doesn't exist: {note}")
        
        note_offset = note_map[note]
        midi_value = 12 + (octave * 12) + note_offset
        
        if not (0 <= midi_value <= 127):
            raise InvalidOctaveError(f"Resulting MIDI value out of range: {midi_value}")
            
        return midi_value
    
    except(InvalidNoteError, InvalidOctaveError):
        raise
    
    except Exception as e:
        raise InvalidNoteError(f"Unexpected error processing note: {note_name}")

def midiFreq(note_name: str, round_digits: int = 2, concert_pitch: float = CONCERT_PITCH) -> float:
    """Convert note name to frequency."""
    try:
        pitch = midiKey(note_name)
        freq = (2 ** ((pitch - 69) / 12)) * concert_pitch
        return round(freq, round_digits) if round_digits >= 0 else freq
    except (InvalidNoteError, InvalidOctaveError):
        raise


def freqToMidi(freq: float, concert_pitch: float = CONCERT_PITCH) -> int:
    """Convert frequency to MIDI note number."""
    if freq <= 0:
        raise InvalidFrequencyError("Frequency must be positive")
    
    try:
        midi = 12 * (math.log2(freq / concert_pitch)) + 69
        rounded_midi = round(midi)
        
        if not (0 <= rounded_midi <= 127):
            raise InvalidFrequencyError(f"Frequency {freq}Hz results in out-of-range MIDI note: {rounded_midi}")
            
        return rounded_midi
    except ValueError as e:
        raise InvalidFrequencyError(f"Invalid frequency value: {freq}") from e


def midiToNoteName(midi_number: int, use_sharps: bool = True) -> str:
    """Convert MIDI number to note name."""
    if not (0 <= midi_number <= 127):
        raise InvalidNoteError(f"MIDI number out of range (0-127): {midi_number}")
    
    notes = NOTE_NAMES_SHARP if use_sharps else NOTE_NAMES_FLAT
    octave = (midi_number // 12) - 1
    note = notes[midi_number % 12]
    return f"{note}{octave}"


def is_valid_midi_range(note_name: str) -> bool:
    """Check if note is within standard MIDI range (0-127)."""
    try:
        midi_val = midiKey(note_name)
        return 0 <= midi_val <= 127
    except (InvalidNoteError, InvalidOctaveError):
        return False


def notes_to_frequencies(note_list: List[str], round_digits: int = 2, 
                        concert_pitch: float = CONCERT_PITCH) -> List[Union[float, str]]:
    """Convert list of notes to frequencies."""
    results = []
    for note in note_list:
        try:
            freq = midiFreq(note, round_digits, concert_pitch)
            results.append(freq)
        except (InvalidNoteError, InvalidOctaveError) as e:
            results.append(str(e))
    return results


def notes_to_midi(note_list: List[str]) -> List[Union[int, str]]:
    """Convert list of notes to MIDI numbers."""
    results = []
    for note in note_list:
        try:
            midi = midiKey(note)
            results.append(midi)
        except (InvalidNoteError, InvalidOctaveError) as e:
            results.append(str(e))
    return results
