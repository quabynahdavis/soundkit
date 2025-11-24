#!/usr/bin/env python3
"""
Advanced applications of SoundKit
"""

import soundkit as sk


class MusicTheoryAnalyzer:
    """A class to analyze music theory concepts using SoundKit"""

    def __init__(self, concert_pitch=440.0):
        self.concert_pitch = concert_pitch

    def analyze_chord_progression(self, progression, octave=4):
        """Analyze a chord progression"""
        print("Chord Progression Analysis:")
        print("-" * 40)

        for i, (root, quality) in enumerate(progression, 1):
            # Get chord information
            chord_notes = sk.chords.get_chord_notes(root, quality, octave)
            chord_freq = sk.chords.get_chord_frequencies(
                root, quality, octave, concert_pitch=self.concert_pitch
            )
            note_names = [sk.notes.midiToNoteName(n) for n in chord_notes]

            print(f"Chord {i}: {root}{quality}")
            print(f"  Notes: {note_names}")
            print(f"  MIDI: {chord_notes}")
            print(f"  Frequencies: {[f'{f:.2f}' for f in chord_freq]} Hz")
            print()

    def compare_scales(self, root_note, scale_types, octave=4, num_octaves=1):
        """Compare different scales starting on the same root"""
        print(f"Scale Comparison - Root: {root_note}")
        print("-" * 40)

        for scale_type in scale_types:
            scale_notes = sk.scales.get_scale_notes(
                root_note, scale_type, octave, num_octaves
            )
            note_names = [sk.notes.midiToNoteName(n) for n in scale_notes]

            print(f"{scale_type.title()} Scale:")
            print(f"  Notes: {note_names}")
            print(f"  MIDI: {scale_notes}")
            print()

    def calculate_interval_relationships(self, base_note="C4"):
        """Calculate interval relationships from a base note"""
        base_midi = sk.notes.midiKey(base_note)

        intervals = {
            "Unison": 0,
            "Minor 2nd": 1,
            "Major 2nd": 2,
            "Minor 3rd": 3,
            "Major 3rd": 4,
            "Perfect 4th": 5,
            "Tritone": 6,
            "Perfect 5th": 7,
            "Minor 6th": 8,
            "Major 6th": 9,
            "Minor 7th": 10,
            "Major 7th": 11,
            "Octave": 12,
        }

        print(f"Interval Relationships from {base_note}:")
        print("-" * 40)

        for name, semitones in intervals.items():
            target_midi = base_midi + semitones
            if target_midi <= 127:  # Stay in MIDI range
                target_note = sk.notes.midiToNoteName(target_midi)
                base_freq = sk.notes.midiFreq(
                    base_note, concert_pitch=self.concert_pitch
                )
                target_freq = sk.notes.midiFreq(
                    target_note, concert_pitch=self.concert_pitch
                )
                ratio = target_freq / base_freq

                print(
                    f"{name:12} -> {target_note:4} "
                    f"(Ratio: {ratio:.3f}, {semitones} semitones)"
                )


class TuningSystem:
    """A class to work with different tuning systems"""

    def __init__(self):
        self.systems = {
            "equal_temperament": self.equal_temperament,
            "just_intonation": self.just_intonation,
            "pythagorean": self.pythagorean_tuning,
        }

    def equal_temperament(self, base_freq, semitones):
        """Calculate frequency in equal temperament"""
        return base_freq * (2 ** (semitones / 12))

    def just_intonation(self, base_freq, interval_ratio):
        """Calculate frequency in just intonation"""
        return base_freq * interval_ratio

    def pythagorean_tuning(self, base_freq, perfect_fifths):
        """Calculate frequency in Pythagorean tuning"""
        return base_freq * (3 / 2) ** perfect_fifths

    def compare_tuning_systems(self, base_note="A4", base_freq=440.0):
        """Compare different tuning systems for a scale"""
        intervals = {
            "Unison": 0,
            "Major 2nd": 2,
            "Major 3rd": 4,
            "Perfect 4th": 5,
            "Perfect 5th": 7,
            "Major 6th": 9,
            "Major 7th": 11,
            "Octave": 12,
        }

        just_ratios = {
            "Unison": 1 / 1,
            "Major 2nd": 9 / 8,
            "Major 3rd": 5 / 4,
            "Perfect 4th": 4 / 3,
            "Perfect 5th": 3 / 2,
            "Major 6th": 5 / 3,
            "Major 7th": 15 / 8,
            "Octave": 2 / 1,
        }

        print("Tuning System Comparison:")
        print("-" * 50)
        print(
            f"{'Interval':<12} {'Equal Temp':<12} {'Just Intonation':<16} {'Difference (cents)':<18}"
        )
        print("-" * 50)

        for name, semitones in intervals.items():
            # Equal temperament
            et_freq = self.equal_temperament(base_freq, semitones)

            # Just intonation
            if name in just_ratios:
                ji_freq = self.just_intonation(base_freq, just_ratios[name])

                # Calculate difference in cents
                diff_cents = sk.converters.frequency_to_cents(et_freq, ji_freq)

                print(
                    f"{name:<12} {et_freq:<12.2f} {ji_freq:<16.2f} {diff_cents:<18.2f}"
                )


def create_chord_progression_exercise():
    """Create a chord progression practice exercise"""
    print("Chord Progression Practice Exercise")
    print("=" * 50)

    # Common progressions
    progressions = {
        "Blues (12-bar)": [
            ("C", "7"),
            ("C", "7"),
            ("C", "7"),
            ("C", "7"),
            ("F", "7"),
            ("F", "7"),
            ("C", "7"),
            ("C", "7"),
            ("G", "7"),
            ("F", "7"),
            ("C", "7"),
            ("G", "7"),
        ],
        "Jazz II-V-I": [
            ("D", "min7"),
            ("G", "7"),
            ("C", "maj7"),
            ("E", "min7"),
            ("A", "7"),
            ("D", "maj7"),
            ("A", "min7"),
            ("D", "7"),
            ("G", "maj7"),
        ],
        "Pop Progression": [("C", "maj"), ("G", "maj"), ("A", "min"), ("F", "maj")],
    }

    for name, progression in progressions.items():
        print(f"\n{name}:")
        chords_per_line = 4
        for i in range(0, len(progression), chords_per_line):
            line_chords = progression[i : i + chords_per_line]
            line = " | ".join([f"{root}{quality}" for root, quality in line_chords])
            print(f"  {line}")

        # Show first chord details
        if progression:
            first_root, first_quality = progression[0]
            chord_notes = sk.chords.get_chord_notes(first_root, first_quality, 4)
            note_names = [sk.notes.midiToNoteName(n) for n in chord_notes]
            print(f"  Example: {first_root}{first_quality} = {note_names}")


def main():
    """Run advanced applications"""
    print("SoundKit Advanced Applications")
    print("=" * 60)

    # Music theory analysis
    analyzer = MusicTheoryAnalyzer(concert_pitch=440.0)

    print("\n1. Music Theory Analysis")
    print("-" * 30)

    # Analyze a progression
    progression = [("C", "maj7"), ("D", "min7"), ("G", "7"), ("C", "maj7")]
    analyzer.analyze_chord_progression(progression)

    # Compare scales
    scales_to_compare = ["major", "minor", "dorian", "mixolydian"]
    analyzer.compare_scales("C", scales_to_compare)

    # Interval relationships
    analyzer.calculate_interval_relationships("C4")

    # Tuning system comparison
    print("\n2. Tuning System Analysis")
    print("-" * 30)
    tuning_system = TuningSystem()
    tuning_system.compare_tuning_systems()

    # Chord progression exercises
    print("\n3. Practice Exercises")
    print("-" * 30)
    create_chord_progression_exercise()

    # Advanced scale demonstration
    print("\n4. Advanced Scale Applications")
    print("-" * 30)

    # Show exotic scales
    exotic_scales = ["harmonic_minor", "melodic_minor", "whole_tone", "blues"]
    for scale in exotic_scales:
        scale_notes = sk.scales.get_scale_notes("C", scale, 4)
        note_names = [sk.notes.midiToNoteName(n) for n in scale_notes]
        print(f"C {scale}: {note_names}")

    print("\n" + "=" * 60)
    print("Advanced applications complete!")


if __name__ == "__main__":
    main()
