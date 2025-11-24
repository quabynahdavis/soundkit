"""
SoundKit - A Comprehensive Python framework for musical note processing, MIDI manipulation and music theory operations.
"""

__version__ = "1.0.0"
__author__ = "Quabynah Davis"
__email__ = "exceldavisville@gmail.com"

from .core import notes, chords, scales
from .utils import validators, converters
from .constants import *
from .exceptions import *

__all__ = [
    # Exceptions
    "SoundKitError",
    "InvalidNoteError",
    "InvalidOctaveError",
    "InvalidFrequencyError",
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
]
