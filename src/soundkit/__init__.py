"""
SoundKit - A Comprehensive Python framework for musical note processing, MIDI manipulation and music theory operations.
"""

__version__ = "1.0.5"
__author__ = "Quabynah Davis"
__email__ = "exceldavisville@gmail.com"

# Base Modules
from . import core
from . import utils
from .constants import *
from .exceptions import *

from .core import * # Core Modules
from .utils import * # Util Modules


__all__ = [
    
    # Base Utils
    "core", "utils",

    # Core modules
    "notes",
    "scales",
    "chords",
    
    # Utils modules
    "validators",
    "converters",
    
    # Constants
    "CONCERT_PITCH",
    "MIDI_RANGE",
    "REFERENCE_FREQUENCIES",
    
    # Exceptions
    "SoundKitError",
    "InvalidNoteError",
    "InvalidOctaveError",
    "InvalidFrequencyError",
    
    # Validator module
    "validate_note_name",
    "validate_midi_range",
    "validate_frequency",
    "normalize_note_name",
    "validate_octave",
    
    # Converter module
    "frequency_to_cents",
    "cents_to_ratio",
    "frequency_to_cents",
    "ratio_to_cents",
    "semitones_to_ratio",
    "ratio_to_semitones",
    "normalize_frequency",

    # Notes modules
    "normalize_note_name", "midiFreq", "midiKey", "midiToNoteName",
    "freqToMidi", "is_valid_midi_range","notes_to_frequencies","notes_to_midi",
    
    # Scales module
    "get_scale_frequencies", "get_scale_names", "get_scale_notes",
    
    # Chords modules
    "get_chord_names", "get_chord_frequencies", "get_chord_notes",

]
