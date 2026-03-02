from . import notes
from . import chords
from . import scales

from .notes import (normalize_note_name, midiFreq, midiKey, midiToNoteName, freqToMidi,
                    is_valid_midi_range, notes_to_frequencies, notes_to_midi)
from .scales import get_scale_frequencies,get_scale_names,get_scale_notes
from .chords import *

__all__ = [
    # Core modules
    "notes", "chords", "scales",
    
    # Notes modules
    "normalize_note_name", "midiFreq", "midiKey", "midiToNoteName",
    "freqToMidi", "is_valid_midi_range","notes_to_frequencies","notes_to_midi",
    
    # Scales module
    "get_scale_frequencies", "get_scale_names", "get_scale_notes",
    
    # Chords modules
    "get_chord_names", "get_chord_frequencies", "get_chord_notes",

]