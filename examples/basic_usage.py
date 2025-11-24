#!/usr/bin/env python3
"""
Basic usage examples for SoundKit
"""

import soundkit as sk


def demonstrate_notes():
    """Demonstrate note conversion functionality"""
    print("=== Note Conversion Examples ===")

    # Basic note to MIDI conversion
    notes = ["C4", "E4", "G4", "A4", "Bb4"]
    print("\n1. Note to MIDI Conversion:")
    for note in notes:
        midi = sk.notes.midiKey(note)
        print(f"   {note} -> MIDI: {midi}")

    # Note to frequency conversion
    print("\n2. Note to Frequency Conversion:")
    for note in notes:
        freq = sk.notes.midiFreq(note)
        print(f"   {note} -> {freq} Hz")

    # Reverse conversion
    print("\n3. MIDI to Note Conversion:")
    midi_numbers = [60, 62, 64, 65, 67, 69, 71]  # C major scale
    for midi in midi_numbers:
        note_name = sk.notes.midiToNoteName(midi)
        print(f"   MIDI {midi} -> {note_name}")

    # Batch processing
    print("\n4. Batch Processing:")
    note_list = ["C4", "D4", "E4", "F4", "G4"]
    midi_results = sk.notes.notes_to_midi(note_list)
    freq_results = sk.notes.notes_to_frequencies(note_list)

    for i, note in enumerate(note_list):
        print(f"   {note}: MIDI {midi_results[i]}, Freq {freq_results[i]} Hz")


def demonstrate_chords():
    """Demonstrate chord generation functionality"""
    print("\n=== Chord Generation Examples ===")

    # Basic chords
    chords = [
        ("C", "maj"),
        ("C", "min"),
        ("C", "7"),
        ("C", "maj7"),
        ("G", "maj"),
        ("D", "min"),
        ("A", "7"),
    ]

    print("\n1. Basic Chords:")
    for root, quality in chords:
        chord_notes = sk.chords.get_chord_notes(root, quality, 4)
        chord_freq = sk.chords.get_chord_frequencies(root, quality, 4)
        print(f"   {root}{quality}: {chord_notes} -> {chord_freq} Hz")

    # Chord inversions
    print("\n2. Chord Inversions:")
    inversions = [0, 1, 2]
    for inversion in inversions:
        chord_notes = sk.chords.get_chord_notes("C", "maj", 4, inversion)
        print(f"   C major inversion {inversion}: {chord_notes}")

    # Available chord types
    print("\n3. Available Chord Types:")
    chord_types = sk.chords.get_chord_names()
    print(f"   Supported chords: {', '.join(chord_types[:8])}...")


def demonstrate_scales():
    """Demonstrate scale generation functionality"""
    print("\n=== Scale Generation Examples ===")

    # Common scales
    scales = [
        ("C", "major"),
        ("A", "minor"),
        ("C", "pentatonic_major"),
        ("A", "pentatonic_minor"),
        ("C", "blues"),
        ("D", "dorian"),
    ]

    print("\n1. Common Scales:")
    for root, scale_type in scales:
        scale_notes = sk.scales.get_scale_notes(root, scale_type, 4)
        print(f"   {root} {scale_type}: {scale_notes}")

    # Multi-octave scales
    print("\n2. Multi-Octave Scales:")
    c_major_2oct = sk.scales.get_scale_notes("C", "major", 4, 2)
    print(f"   C major (2 octaves): {c_major_2oct}")

    # Scale frequencies
    print("\n3. Scale Frequencies:")
    c_major_freq = sk.scales.get_scale_frequencies("C", "major", 4)
    print(f"   C major frequencies: {[f'{f:.1f}' for f in c_major_freq]} Hz")

    # Available scale types
    print("\n4. Available Scale Types:")
    scale_types = sk.scales.get_scale_names()
    print(f"   Supported scales: {', '.join(scale_types[:8])}...")


def demonstrate_utils():
    """Demonstrate utility functions"""
    print("\n=== Utility Functions Examples ===")

    # Validation
    print("\n1. Input Validation:")
    test_inputs = ["C4", "H4", "C11", "C", "C#4"]
    for test_input in test_inputs:
        is_valid = sk.validators.validate_note_name(test_input)
        print(f"   '{test_input}' valid: {is_valid}")

    # Frequency conversion utilities
    print("\n2. Frequency Conversion Utilities:")
    # Cents calculation
    cents = sk.converters.frequency_to_cents(440, 444)
    print(f"   440Hz to 444Hz: {cents:.2f} cents")

    # Ratio conversion
    ratio = sk.converters.cents_to_ratio(100)
    print(f"   100 cents ratio: {ratio:.4f}")

    # Semitone conversion
    semitones = sk.converters.ratio_to_semitones(1.5)
    print(f"   Perfect fifth (1.5 ratio): {semitones:.1f} semitones")


def demonstrate_music_theory():
    """Demonstrate music theory applications"""
    print("\n=== Music Theory Applications ===")

    # Chord progression analysis
    print("\n1. II-V-I Progression Analysis:")
    progression = [("D", "min7"), ("G", "7"), ("C", "maj7")]

    for root, quality in progression:
        chord_notes = sk.chords.get_chord_notes(root, quality, 4)
        chord_freq = sk.chords.get_chord_frequencies(root, quality, 4)
        note_names = [sk.notes.midiToNoteName(n) for n in chord_notes]
        print(f"   {root}{quality}: {note_names} -> {chord_freq} Hz")

    # Scale modes
    print("\n2. Modes of C Major:")
    modes = ["major", "dorian", "phrygian", "lydian", "mixolydian", "minor", "locrian"]
    for mode in modes:
        scale_notes = sk.scales.get_scale_notes("C", mode, 4)
        note_names = [sk.notes.midiToNoteName(n) for n in scale_notes]
        print(f"   C {mode}: {note_names}")

    # Tuning comparison
    print("\n3. Tuning Standards Comparison:")
    tunings = {
        "Modern Standard": 440.0,
        "Baroque": 415.0,
        "Verdi": 432.0,
        "Modern High": 442.0,
    }

    note = "A4"
    for name, pitch in tunings.items():
        freq = sk.notes.midiFreq(note, concert_pitch=pitch)
        print(f"   {name} (A4={pitch}Hz): {note} = {freq:.1f} Hz")


def main():
    """Run all demonstrations"""
    print("SoundKit Demonstration")
    print("=" * 50)

    demonstrate_notes()
    demonstrate_chords()
    demonstrate_scales()
    demonstrate_utils()
    demonstrate_music_theory()

    print("\n" + "=" * 50)
    print("Demonstration complete!")


if __name__ == "__main__":
    main()
