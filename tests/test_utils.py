import unittest
from src.soundkit.utils.validators import (
    validate_note_name,
    validate_midi_range,
    validate_frequency,
    validate_octave,
    normalize_note_name,
)
from src.soundkit.utils.converters import (
    frequency_to_cents,
    cents_to_ratio,
    ratio_to_cents,
    semitones_to_ratio,
    ratio_to_semitones,
    normalize_frequency,
)
from src.soundkit.exceptions import InvalidFrequencyError


class TestValidators(unittest.TestCase):

    def test_validate_note_name(self):
        """Test note name validation"""
        self.assertTrue(validate_note_name("C4"))
        self.assertTrue(validate_note_name("C#4"))
        self.assertTrue(validate_note_name("Db4"))
        self.assertTrue(validate_note_name("A-1"))
        self.assertTrue(validate_note_name("G9"))

        self.assertFalse(validate_note_name("H4"))  # Invalid note
        self.assertFalse(validate_note_name("C"))  # Missing octave
        self.assertFalse(validate_note_name("4"))  # Missing note
        self.assertFalse(validate_note_name("C4extra"))  # Extra chars

    def test_validate_midi_range(self):
        """Test MIDI range validation"""
        self.assertTrue(validate_midi_range(0))
        self.assertTrue(validate_midi_range(60))
        self.assertTrue(validate_midi_range(127))

        self.assertFalse(validate_midi_range(-1))
        self.assertFalse(validate_midi_range(128))

    def test_validate_frequency(self):
        """Test frequency validation"""
        self.assertTrue(validate_frequency(440.0))
        self.assertTrue(validate_frequency(20.0))  # Low end of hearing
        self.assertTrue(validate_frequency(20000.0))  # High end of hearing

        self.assertFalse(validate_frequency(-100.0))
        self.assertFalse(validate_frequency(0.0))
        self.assertFalse(validate_frequency(30000.0))  # Beyond hearing range

    def test_validate_octave(self):
        """Test octave validation"""
        self.assertTrue(validate_octave(-1))
        self.assertTrue(validate_octave(0))
        self.assertTrue(validate_octave(4))
        self.assertTrue(validate_octave(10))

        self.assertFalse(validate_octave(-2))
        self.assertFalse(validate_octave(11))

    def test_normalize_note_name(self):
        """Test note name normalization"""
        self.assertEqual(normalize_note_name("c4"), "C4")
        self.assertEqual(normalize_note_name("C#4"), "C#4")
        self.assertEqual(normalize_note_name("db4"), "DB4")
        self.assertEqual(normalize_note_name("C ♯4"), "C#4")
        self.assertEqual(normalize_note_name("C ♭4"), "CB4")
        self.assertEqual(normalize_note_name("C-4"), "C4")
        self.assertEqual(normalize_note_name("C 4"), "C4")


class TestConverters(unittest.TestCase):

    def test_frequency_to_cents(self):
        """Test frequency to cents conversion"""
        # Octave difference
        self.assertAlmostEqual(frequency_to_cents(440, 880), 1200.0, places=2)

        # Perfect fifth (700 cents)
        self.assertAlmostEqual(frequency_to_cents(440, 660), 700.0, places=2)

        # Small difference
        cents = frequency_to_cents(440, 444)
        self.assertGreater(cents, 0)
        self.assertLess(cents, 20)

    def test_frequency_to_cents_invalid(self):
        """Test invalid frequency for cents conversion"""
        with self.assertRaises(InvalidFrequencyError):
            frequency_to_cents(-100, 440)

        with self.assertRaises(InvalidFrequencyError):
            frequency_to_cents(440, 0)

    def test_cents_to_ratio(self):
        """Test cents to ratio conversion"""
        # Octave
        self.assertAlmostEqual(cents_to_ratio(1200), 2.0, places=2)

        # Perfect fifth
        self.assertAlmostEqual(cents_to_ratio(700), 1.5, places=2)

        # Semitone
        self.assertAlmostEqual(cents_to_ratio(100), 1.05946, places=4)

    def test_ratio_to_cents(self):
        """Test ratio to cents conversion"""
        # Octave
        self.assertAlmostEqual(ratio_to_cents(2.0), 1200.0, places=2)

        # Perfect fifth
        self.assertAlmostEqual(ratio_to_cents(1.5), 700.0, places=2)

    def test_ratio_to_cents_invalid(self):
        """Test invalid ratio for cents conversion"""
        with self.assertRaises(InvalidFrequencyError):
            ratio_to_cents(-1.0)

        with self.assertRaises(InvalidFrequencyError):
            ratio_to_cents(0.0)

    def test_semitones_to_ratio(self):
        """Test semitones to ratio conversion"""
        self.assertAlmostEqual(semitones_to_ratio(12), 2.0, places=2)  # Octave
        self.assertAlmostEqual(semitones_to_ratio(7), 1.5, places=2)  # Perfect fifth
        self.assertAlmostEqual(semitones_to_ratio(0), 1.0, places=2)  # Unison

    def test_ratio_to_semitones(self):
        """Test ratio to semitones conversion"""
        self.assertAlmostEqual(ratio_to_semitones(2.0), 12.0, places=2)  # Octave
        self.assertAlmostEqual(ratio_to_semitones(1.5), 7.0, places=2)  # Perfect fifth
        self.assertAlmostEqual(ratio_to_semitones(1.0), 0.0, places=2)  # Unison

    def test_normalize_frequency(self):
        """Test frequency normalization"""
        # Should normalize to nearest A
        self.assertAlmostEqual(normalize_frequency(441.0), 440.0, places=0)
        self.assertAlmostEqual(normalize_frequency(439.0), 440.0, places=0)

        # With custom reference
        self.assertAlmostEqual(normalize_frequency(443.0, 442.0), 442.0, places=0)

    def test_normalize_frequency_invalid(self):
        """Test invalid frequency normalization"""
        with self.assertRaises(InvalidFrequencyError):
            normalize_frequency(-100.0)

        with self.assertRaises(InvalidFrequencyError):
            normalize_frequency(0.0)


if __name__ == "__main__":
    unittest.main()
