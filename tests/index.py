

```python
#!/usr/bin/env python3
"""
Basic usage examples for SoundKit
"""

import soundkit as sk

def main():
    print("=== SoundKit Examples ===\n")
    
    # Basic note conversion
    print("1. Basic Note Co.gitignorenversion:")
    notes = ["C4", "A4", "Gb3", "D#5"]
    for note in notes:
        midi = sk.midiKey(note)
        freq = sk.midiFreq(note)
        print(f"  {note} -> MIDI: {midi}, Frequency: {freq}Hz")
    
    # Chord examples
    print("\n2. Chord Examples:")
    chords = [("C", "maj"), ("D", "min7"), ("G", "7")]
    for root, chord_type in chords:
        chord_notes = sk.get_chord_notes(root, chord_type, 4)
        chord_freqs = sk.get_chord_frequencies(root, chord_type, 4)
        print(f"  {root}{chord_type}: {chord_notes} -> {chord_freqs}Hz")
    
    # Scale examples
    print("\n3. Scale Examples:")
    scales = [("C", "major"), ("A", "minor"), ("G", "pentatonic_major")]
    for root, scale_type in scales:
        scale_notes = sk.get_scale_notes(root, scale_type, 4, 1)
        print(f"  {root} {scale_type}: {scale_notes}")
    
    # Reverse conversion
    print("\n4. Reverse Conversion:")
    midi_note = 60
    note_name = sk.midiToNoteName(midi_note)
    freq = sk.midiFreq(note_name)
    print(f"  MIDI {midi_note} -> {note_name} -> {freq}Hz")

if __name__ == "__main__":
    main()