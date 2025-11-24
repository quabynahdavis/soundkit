import unittest
import math
from src.soundkit.core.notes import midiKey, midiFreq, freqToMidi, midiToNoteName
from src.soundkit.core.notes import (
    notes_to_midi,
    notes_to_frequencies,
    is_valid_midi_range,
)
from src.soundkit.exceptions import (
    InvalidNoteError,
    InvalidOctaveError,
    InvalidFrequencyError,
)


class TestNotes(unittest.TestCase):

    def test_midiKey_basic_notes(self):
        """Test basic note to MIDI conversion"""
        self.assertEqual(midiKey("C4"), 60)
        self.assertEqual(midiKey("A4"), 69)
        self.assertEqual(midiKey("C0"), 12)
        self.assertEqual(midiKey("C-1"), 0)
        self.assertEqual(midiKey("G9"), 127)

    def test_midiKey_sharps(self):
        """Test sharp notes"""
        self.assertEqual(midiKey("C#4"), 61)
        self.assertEqual(midiKey("D#4"), 63)
        self.assertEqual(midiKey("F#4"), 66)
        self.assertEqual(midiKey("G#4"), 68)
        self.assertEqual(midiKey("A#4"), 70)

    def test_midiKey_flats(self):
        """Test flat notes"""
        self.assertEqual(midiKey("Db4"), 61)
        self.assertEqual(midiKey("Eb4"), 63)
        self.assertEqual(midiKey("Gb4"), 66)
        self.assertEqual(midiKey("Ab4"), 68)
        self.assertEqual(midiKey("Bb4"), 70)

    def test_midiKey_case_insensitive(self):
        """Test case insensitivity"""
        self.assertEqual(midiKey("c4"), 60)
        self.assertEqual(midiKey("C#4"), 61)
        self.assertEqual(midiKey("db4"), 61)

    def test_midiKey_invalid_notes(self):
        """Test invalid note handling"""
        with self.assertRaises(InvalidNoteError):
            midiKey("H4")  # Invalid note name

        with self.assertRaises(InvalidNoteError):
            midiKey("C")  # Missing octave

        with self.assertRaises(InvalidNoteError):
            midiKey("C#4extra")  # Extra characters

    def test_midiKey_invalid_octaves(self):
        """Test invalid octave handling"""
        with self.assertRaises(InvalidOctaveError):
            midiKey("C11")  # Octave too high

        with self.assertRaises(InvalidOctaveError):
            midiKey("C-2")  # Octave too low

    def test_midiFreq_basic(self):
        """Test note to frequency conversion"""
        self.assertAlmostEqual(midiFreq("A4"), 440.0, places=2)
        self.assertAlmostEqual(midiFreq("C4"), 261.63, places=2)
        self.assertAlmostEqual(midiFreq("A3"), 220.0, places=2)

    def test_midiFreq_rounding(self):
        """Test frequency rounding"""
        freq_no_round = midiFreq("C4", round_digits=-1)
        self.assertIsInstance(freq_no_round, float)

        freq_rounded = midiFreq("C4", round_digits=4)
        self.assertEqual(len(str(freq_rounded).split(".")[1]), 4)

    def test_midiFreq_custom_concert_pitch(self):
        """Test custom concert pitch"""
        freq_442 = midiFreq("A4", concert_pitch=442.0)
        self.assertAlmostEqual(freq_442, 442.0, places=2)

    def test_freqToMidi_basic(self):
        """Test frequency to MIDI conversion"""
        self.assertEqual(freqToMidi(440.0), 69)
        self.assertEqual(freqToMidi(261.63), 60)
        self.assertEqual(freqToMidi(880.0), 81)

    def test_freqToMidi_custom_concert_pitch(self):
        """Test frequency to MIDI with custom concert pitch"""
        self.assertEqual(freqToMidi(442.0, concert_pitch=442.0), 69)

    def test_freqToMidi_invalid_frequencies(self):
        """Test invalid frequency handling"""
        with self.assertRaises(InvalidFrequencyError):
            freqToMidi(-100.0)

        with self.assertRaises(InvalidFrequencyError):
            freqToMidi(0.0)

    def test_midiToNoteName_basic(self):
        """Test MIDI to note name conversion"""
        self.assertEqual(midiToNoteName(60), "C4")
        self.assertEqual(midiToNoteName(69), "A4")
        self.assertEqual(midiToNoteName(0), "C-1")
        self.assertEqual(midiToNoteName(127), "G9")

    def test_midiToNoteName_flats(self):
        """Test MIDI to note name with flats"""
        self.assertEqual(midiToNoteName(61, use_sharps=False), "Db4")
        self.assertEqual(midiToNoteName(63, use_sharps=False), "Eb4")
        self.assertEqual(midiToNoteName(66, use_sharps=False), "Gb4")

    def test_midiToNoteName_invalid_midi(self):
        """Test invalid MIDI number handling"""
        with self.assertRaises(InvalidNoteError):
            midiToNoteName(-1)

        with self.assertRaises(InvalidNoteError):
            midiToNoteName(128)

    def test_notes_to_midi(self):
        """Test batch note to MIDI conversion"""
        notes = ["C4", "E4", "G4", "A4", "invalid_note"]
        result = notes_to_midi(notes)

        self.assertEqual(result[0], 60)
        self.assertEqual(result[1], 64)
        self.assertEqual(result[2], 67)
        self.assertEqual(result[3], 69)
        self.assertIsInstance(result[4], str)  # Error message

    def test_notes_to_frequencies(self):
        """Test batch note to frequency conversion"""
        notes = ["C4", "E4", "G4", "A4"]
        frequencies = notes_to_frequencies(notes)

        self.assertAlmostEqual(frequencies[0], 261.63, places=2) # type: ignore
        self.assertAlmostEqual(frequencies[1], 329.63, places=2)
        self.assertAlmostEqual(frequencies[2], 392.0, places=2)
        self.assertAlmostEqual(frequencies[3], 440.0, places=2)

    def test_is_valid_midi_range(self):
        """Test MIDI range validation"""
        self.assertTrue(is_valid_midi_range("C4"))
        self.assertTrue(is_valid_midi_range("C-1"))
        self.assertTrue(is_valid_midi_range("G9"))
        self.assertFalse(is_valid_midi_range("C11"))
        self.assertFalse(is_valid_midi_range("H4"))


if __name__ == "__main__":
    unittest.main()
