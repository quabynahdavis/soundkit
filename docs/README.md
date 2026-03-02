# SoundKit

**A Comprehensive Python Framework for Musical Note Processing, MIDI Manipulation and Music Theory Operations**

SoundKit is a powerful Python framework designed for musicians, developers, and audio engineers working with musical notes, MIDI data, and music theory. It provides intuitive APIs for note conversion, chord generation, scale creation, and comprehensive music theory operations.

## Features

- 🎵 **Note Conversion**: Convert between note names, MIDI numbers, and frequencies
- 🎹 **Chord Generation**: Create chords with various types and inversions
- 🎼 **Scale Generation**: Generate musical scales with multiple octaves
- 🔍 **Validation**: Comprehensive input validation and error handling
- 📊 **Utilities**: Advanced conversion tools and music theory utilities
- 🎯 **Music Theory**: Built-in music theory operations and constants

## Installation

```bash
pip install soundkit
```

## Quick Start

```python
import soundkit as sk

# Basic note conversion
print(sk.notes.midiKey("C4"))      # 60
print(sk.notes.midiFreq("A4"))     # 440.0

# Create chords
c_major = sk.chords.get_chord_notes("C", "maj", 4)
print(c_major)  # [60, 64, 67]

# Generate scales
c_major_scale = sk.scales.get_scale_notes("C", "major", 4, 2)
print(c_major_scale)  # [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
```

## Core Modules

### Notes Module

The `notes` module handles all note-related conversions and operations.

#### Basic Note Conversion

```python
import soundkit as sk

# Convert note name to MIDI number
midi_number = sk.notes.midiKey("C4")        # 60
midi_number = sk.notes.midiKey("A4")        # 69
midi_number = sk.notes.midiKey("Gb3")       # 54

# Convert note name to frequency
frequency = sk.notes.midiFreq("A4")         # 440.0
frequency = sk.notes.midiFreq("C4")         # 261.63
frequency = sk.notes.midiFreq("C4", round_digits=4)  # 261.6256

# Convert frequency to MIDI number
midi_number = sk.notes.freqToMidi(440.0)    # 69
midi_number = sk.notes.freqToMidi(261.63)   # 60

# Convert MIDI number to note name
note_name = sk.notes.midiToNoteName(60)     # "C4"
note_name = sk.notes.midiToNoteName(69)     # "A4"
note_name = sk.notes.midiToNoteName(60, use_sharps=False)  # "C4" (no effect for C)
```

#### Supported Note Formats

SoundKit supports various note naming conventions:

```python
# Sharp notes
sk.notes.midiKey("C#4")    # 61
sk.notes.midiKey("D#4")    # 63
sk.notes.midiKey("F#4")    # 66

# Flat notes
sk.notes.midiKey("Db4")    # 61
sk.notes.midiKey("Eb4")    # 63
sk.notes.midiKey("Gb4")    # 66

# Mixed notation
sk.notes.midiKey("C4")     # 60
sk.notes.midiKey("C#4")    # 61
sk.notes.midiKey("Db4")    # 61 (same as C#4)
```

#### Batch Processing

```python
import soundkit as sk

# Process multiple notes at once
notes = ["C4", "E4", "G4", "A4", "B4"]

# Convert to MIDI numbers
midi_numbers = sk.notes.notes_to_midi(notes)
print(midi_numbers)  # [60, 64, 67, 69, 71]

# Convert to frequencies
frequencies = sk.notes.notes_to_frequencies(notes)
print(frequencies)  # [261.63, 329.63, 392.0, 440.0, 493.88]

# With custom concert pitch
frequencies = sk.notes.notes_to_frequencies(notes, concert_pitch=442.0)
```

#### Validation

```python
import soundkit as sk

# Check if note is valid
is_valid = sk.notes.is_valid_midi_range("C4")  # True
is_valid = sk.notes.is_valid_midi_range("C11") # False

# Handle invalid notes gracefully
try:
    sk.notes.midiKey("H4")  # Invalid note
except sk.InvalidNoteError as e:
    print(f"Error: {e}")

try:
    sk.notes.midiKey("C11")  # Invalid octave
except sk.InvalidOctaveError as e:
    print(f"Error: {e}")
```

### Chords Module

The `chords` module provides chord generation and manipulation.

#### Basic Chord Generation

```python
import soundkit as sk

# Generate chord notes
c_major = sk.chords.get_chord_notes("C", "maj", 4)
print(c_major)  # [60, 64, 67]

d_minor = sk.chords.get_chord_notes("D", "min", 4)
print(d_minor)  # [62, 65, 69]

g_seventh = sk.chords.get_chord_notes("G", "7", 4)
print(g_seventh)  # [67, 71, 74, 77]
```

#### Available Chord Types

```python
import soundkit as sk

# Get all available chord types
chord_types = sk.chords.get_chord_names()
print(chord_types)
# ['maj', 'major', 'min', 'minor', 'dim', 'diminished', 'aug', 'augmented', 
#  '7', 'dominant7', 'maj7', 'major7', 'min7', 'minor7', 'dim7', 'diminished7', 
#  'half_dim7', 'm7b5', 'sus2', 'sus4', '9', 'maj9']
```

#### Chord Inversions

```python
import soundkit as sk

# Root position
c_major_root = sk.chords.get_chord_notes("C", "maj", 4, inversion=0)
print(c_major_root)  # [60, 64, 67]

# First inversion
c_major_first = sk.chords.get_chord_notes("C", "maj", 4, inversion=1)
print(c_major_first)  # [64, 67, 72]

# Second inversion
c_major_second = sk.chords.get_chord_notes("C", "maj", 4, inversion=2)
print(c_major_second)  # [67, 72, 76]
```

#### Chord Frequencies

```python
import soundkit as sk

# Get chord frequencies
c_major_freq = sk.chords.get_chord_frequencies("C", "maj", 4)
print(c_major_freq)  # [261.63, 329.63, 392.0]

# With custom rounding
c_major_freq = sk.chords.get_chord_frequencies("C", "maj", 4, round_digits=4)
print(c_major_freq)  # [261.6256, 329.6276, 392.0]

# With inversion
c_major_first_freq = sk.chords.get_chord_frequencies("C", "maj", 4, inversion=1)
```

### Scales Module

The `scales` module provides scale generation and music theory operations.

#### Basic Scale Generation

```python
import soundkit as sk

# Generate scale notes
c_major = sk.scales.get_scale_notes("C", "major", 4)
print(c_major)  # [60, 62, 64, 65, 67, 69, 71]

a_minor = sk.scales.get_scale_notes("A", "minor", 4)
print(a_minor)  # [69, 71, 72, 74, 76, 77, 79]

# Multiple octaves
c_major_2octaves = sk.scales.get_scale_notes("C", "major", 4, 2)
print(c_major_2octaves)  # [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
```

#### Available Scale Types

```python
import soundkit as sk

# Get all available scale types
scale_types = sk.scales.get_scale_names()
print(scale_types)
# ['major', 'minor', 'natural_minor', 'harmonic_minor', 'melodic_minor', 
#  'pentatonic_major', 'pentatonic_minor', 'blues', 'dorian', 'phrygian', 
#  'lydian', 'mixolydian', 'locrian', 'whole_tone']
```

#### Scale Frequencies

```python
import soundkit as sk

# Get scale frequencies
c_major_freq = sk.scales.get_scale_frequencies("C", "major", 4)
print(c_major_freq)  # [261.63, 293.66, 329.63, 349.23, 392.0, 440.0, 493.88]

# Multiple octaves with custom rounding
c_major_2oct_freq = sk.scales.get_scale_frequencies("C", "major", 4, 2, round_digits=1)
```

#### Modes and Special Scales

```python
import soundkit as sk

# Modes
d_dorian = sk.scales.get_scale_notes("D", "dorian", 4)
print(d_dorian)  # [62, 64, 65, 67, 69, 71, 72]

# Pentatonic scales
c_pentatonic_major = sk.scales.get_scale_notes("C", "pentatonic_major", 4)
print(c_pentatonic_major)  # [60, 62, 64, 67, 69]

a_pentatonic_minor = sk.scales.get_scale_notes("A", "pentatonic_minor", 4)
print(a_pentatonic_minor)  # [69, 72, 74, 76, 79]

# Blues scale
c_blues = sk.scales.get_scale_notes("C", "blues", 4)
print(c_blues)  # [60, 63, 65, 66, 67, 70]
```

### Utils Module

The `utils` module provides validation and conversion utilities.

#### Validators

```python
import soundkit as sk

# Note validation
is_valid = sk.validators.validate_note_name("C4")        # True
is_valid = sk.validators.validate_note_name("H4")        # False
is_valid = sk.validators.validate_note_name("C#4")       # True
is_valid = sk.validators.validate_note_name("Db4")       # True

# MIDI range validation
is_valid = sk.validators.validate_midi_range(60)         # True
is_valid = sk.validators.validate_midi_range(128)        # False

# Frequency validation
is_valid = sk.validators.validate_frequency(440.0)       # True
is_valid = sk.validators.validate_frequency(-10.0)       # False

# Octave validation
is_valid = sk.validators.validate_octave(4)              # True
is_valid = sk.validators.validate_octave(11)             # False

# Note normalization
normalized = sk.validators.normalize_note_name("c#4")    # "C#4"
normalized = sk.validators.normalize_note_name("db4")    # "DB4"
normalized = sk.validators.normalize_note_name("C ♯4")   # "C#4"
```

#### Converters

```python
import soundkit as sk

# Frequency to cents
cents = sk.converters.frequency_to_cents(440, 444)       # ~15.67
cents = sk.converters.frequency_to_cents(440, 880)       # 1200.0

# Cents to ratio
ratio = sk.converters.cents_to_ratio(100)                # ~1.05946
ratio = sk.converters.cents_to_ratio(1200)               # 2.0

# Ratio conversions
ratio = sk.converters.semitones_to_ratio(12)             # 2.0
semitones = sk.converters.ratio_to_semitones(2.0)        # 12.0

# Frequency normalization
normalized = sk.converters.normalize_frequency(441.0)    # ~440.0
normalized = sk.converters.normalize_frequency(445.0, reference=442.0)
```

### Constants

SoundKit provides useful musical constants:

```python
import soundkit as sk

# Standard concert pitch
print(sk.CONCERT_PITCH)  # 440.0

# MIDI range
print(sk.MIDI_RANGE)     # (0, 127)

# Reference frequencies
print(sk.REFERENCE_FREQUENCIES["A4"])  # 440.0
print(sk.REFERENCE_FREQUENCIES["C4"])  # 261.63

# Use constants in your calculations
custom_freq = sk.notes.midiFreq("A4", concert_pitch=442.0)
```

## Error Handling

SoundKit provides comprehensive error handling with custom exceptions:

```python
import soundkit as sk

try:
    # Invalid note name
    sk.notes.midiKey("H4")
except sk.InvalidNoteError as e:
    print(f"Invalid note: {e}")

try:
    # Invalid octave
    sk.notes.midiKey("C11")
except sk.InvalidOctaveError as e:
    print(f"Invalid octave: {e}")

try:
    # Invalid frequency
    sk.notes.freqToMidi(-100)
except sk.InvalidFrequencyError as e:
    print(f"Invalid frequency: {e}")

try:
    # Invalid chord type
    sk.chords.get_chord_notes("C", "invalid_type", 4)
except sk.InvalidChordError as e:
    print(f"Invalid chord: {e}")

try:
    # Invalid scale type
    sk.scales.get_scale_notes("C", "invalid_scale", 4)
except sk.InvalidScaleError as e:
    print(f"Invalid scale: {e}")
```

## Advanced Examples

### Music Theory Application

```python
import soundkit as sk

def analyze_progression(progression):
    """Analyze a chord progression"""
    for chord in progression:
        root, quality = chord
        notes = sk.chords.get_chord_notes(root, quality, 4)
        frequencies = sk.chords.get_chord_frequencies(root, quality, 4)
        print(f"{root}{quality}: {notes} -> {frequencies}Hz")

# Analyze a II-V-I progression
progression = [("D", "min7"), ("G", "7"), ("C", "maj7")]
analyze_progression(progression)
```

### Scale Visualization

```python
import soundkit as sk

def print_scale_intervals(root_note, scale_type, octave=4):
    """Print scale with note names and frequencies"""
    midi_notes = sk.scales.get_scale_notes(root_note, scale_type, octave)
    
    print(f"{root_note} {scale_type} scale:")
    for midi in midi_notes:
        note_name = sk.notes.midiToNoteName(midi)
        frequency = sk.notes.midiFreq(note_name)
        print(f"  {note_name}: {frequency}Hz")

print_scale_intervals("C", "major")
print_scale_intervals("A", "harmonic_minor")
```

### Tuning Analysis

```python
import soundkit as sk

def compare_tunings(note_name, reference_pitches):
    """Compare frequencies across different tuning standards"""
    print(f"Note: {note_name}")
    for name, pitch in reference_pitches.items():
        freq = sk.notes.midiFreq(note_name, concert_pitch=pitch)
        print(f"  {name} (A4={pitch}Hz): {freq}Hz")

tunings = {
    "Modern Standard": 440.0,
    "Baroque": 415.0,
    "Classical": 430.0,
    "Modern High": 442.0
}

compare_tunings("A4", tunings)
```

## API Reference

### Notes Module

- `midiKey(note_name: str) -> int`: Convert note name to MIDI number
- `midiFreq(note_name: str, round_digits: int = 2, concert_pitch: float = 440.0) -> float`: Convert note name to frequency
- `freqToMidi(frequency: float, concert_pitch: float = 440.0) -> int`: Convert frequency to MIDI number
- `midiToNoteName(midi_number: int, use_sharps: bool = True) -> str`: Convert MIDI number to note name
- `is_valid_midi_range(note_name: str) -> bool`: Check if note is within MIDI range
- `notes_to_midi(note_list: List[str]) -> List[Union[int, str]]`: Convert list of notes to MIDI numbers
- `notes_to_frequencies(note_list: List[str], round_digits: int = 2, concert_pitch: float = 440.0) -> List[Union[float, str]]`: Convert list of notes to frequencies

### Chords Module

- `get_chord_notes(chord_root: str, chord_type: str = 'maj', octave: int = 4, inversion: int = 0) -> List[int]`: Get MIDI notes for a chord
- `get_chord_frequencies(chord_root: str, chord_type: str = 'maj', octave: int = 4, round_digits: int = 2, inversion: int = 0) -> List[float]`: Get frequencies for a chord
- `get_chord_names() -> List[str]`: Get available chord types

### Scales Module

- `get_scale_notes(scale_root: str, scale_type: str = 'major', octave: int = 4, num_octaves: int = 1) -> List[int]`: Get MIDI notes for a scale
- `get_scale_frequencies(scale_root: str, scale_type: str = 'major', octave: int = 4, num_octaves: int = 1, round_digits: int = 2) -> List[float]`: Get frequencies for a scale
- `get_scale_names() -> List[str]`: Get available scale types

### Utils Module

#### Validators

- `validate_note_name(note_name: str) -> bool`: Validate note name format
- `validate_midi_range(midi_number: int) -> bool`: Validate MIDI number range
- `validate_frequency(frequency: float) -> bool`: Validate frequency value
- `validate_octave(octave: int) -> bool`: Validate octave range
- `normalize_note_name(note_name: str) -> str`: Normalize note name format

#### Converters

- `frequency_to_cents(freq1: float, freq2: float) -> float`: Convert frequency ratio to cents
- `cents_to_ratio(cents: float) -> float`: Convert cents to frequency ratio
- `ratio_to_cents(ratio: float) -> float`: Convert frequency ratio to cents
- `semitones_to_ratio(semitones: float) -> float`: Convert semitones to frequency ratio
- `ratio_to_semitones(ratio: float) -> float`: Convert frequency ratio to semitones
- `normalize_frequency(frequency: float, reference: float = 440.0) -> float`: Normalize frequency to nearest reference

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

SoundKit is released under the MIT License. See [LICENSE](LICENSE) for details.

## Support

For bug reports, feature requests, or questions:

- Create an issue on [GitHub](https://github.com/yourusername/soundkit/issues)

- Email: <exceldavisville@gmail.com>

## Version History

- **1.0.0**: Initial release with core note, chord, and scale functionality
- **1.0.5**: Minor type corrections and updates
---

SoundKit is developed and maintained by Quabynah Davis.
