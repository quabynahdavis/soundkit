from typing import List
from .notes import midiKey, midiToNoteName, midiFreq
from ..exceptions import InvalidScaleError, InvalidNoteError

SCALE_TYPES = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
    "pentatonic_major": [0, 2, 4, 7, 9],
    "pentatonic_minor": [0, 3, 5, 7, 10],
    "blues": [0, 3, 5, 6, 7, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10],
    "whole_tone": [0, 2, 4, 6, 8, 10],
}


def get_scale_notes(
    scale_root: str, scale_type: str = "major", octave: int = 4, num_octaves: int = 1
) -> List[int]:
    """Get MIDI notes for common scales."""
    if scale_type not in SCALE_TYPES:
        raise InvalidScaleError(f"Unknown scale type: {scale_type}")

    try:
        root_midi = midiKey(f"{scale_root}{octave}")
        intervals = SCALE_TYPES[scale_type]
        notes = []

        for octave_offset in range(num_octaves):
            for interval in intervals:
                note_midi = root_midi + interval + (12 * octave_offset)
                if note_midi <= 127:  # Stay within MIDI range
                    notes.append(note_midi)

        return notes
    except InvalidNoteError as e:
        raise InvalidScaleError(f"Invalid scale root: {scale_root}") from e


def get_scale_frequencies(
    scale_root: str,
    scale_type: str = "major",
    octave: int = 4,
    num_octaves: int = 1,
    round_digits: int = 2,
) -> List[float]:
    """Get frequencies for a scale."""
    midi_notes = get_scale_notes(scale_root, scale_type, octave, num_octaves)
    return [midiFreq(midiToNoteName(note), round_digits) for note in midi_notes]


def get_scale_names() -> List[str]:
    """Get list of available scale types."""
    return list(SCALE_TYPES.keys())
