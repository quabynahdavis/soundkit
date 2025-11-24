import unittest
from src.soundkit.core.chords import (
    get_chord_notes,
    get_chord_frequencies,
    get_chord_names,
)
from src.soundkit.exceptions import InvalidChordError, InvalidNoteError


class TestChords(unittest.TestCase):

    def test_get_chord_notes_major(self):
        """Test major chord generation"""
        c_major = get_chord_notes("C", "maj", 4)
        self.assertEqual(c_major, [60, 64, 67])

        g_major = get_chord_notes("G", "major", 4)
        self.assertEqual(g_major, [67, 71, 74])

    def test_get_chord_notes_minor(self):
        """Test minor chord generation"""
        c_minor = get_chord_notes("C", "min", 4)
        self.assertEqual(c_minor, [60, 63, 67])

        d_minor = get_chord_notes("D", "minor", 4)
        self.assertEqual(d_minor, [62, 65, 69])

    def test_get_chord_notes_seventh(self):
        """Test seventh chord generation"""
        c_major7 = get_chord_notes("C", "maj7", 4)
        self.assertEqual(c_major7, [60, 64, 67, 71])

        g_dominant7 = get_chord_notes("G", "7", 4)
        self.assertEqual(g_dominant7, [67, 71, 74, 77])

        d_minor7 = get_chord_notes("D", "min7", 4)
        self.assertEqual(d_minor7, [62, 65, 69, 72])

    def test_get_chord_notes_inversions(self):
        """Test chord inversions"""
        # Root position
        c_major_root = get_chord_notes("C", "maj", 4, inversion=0)
        self.assertEqual(c_major_root, [60, 64, 67])

        # First inversion
        c_major_first = get_chord_notes("C", "maj", 4, inversion=1)
        self.assertEqual(c_major_first, [64, 67, 72])

        # Second inversion
        c_major_second = get_chord_notes("C", "maj", 4, inversion=2)
        self.assertEqual(c_major_second, [67, 72, 76])

    def test_get_chord_notes_different_octaves(self):
        """Test chords in different octaves"""
        c_major_3 = get_chord_notes("C", "maj", 3)
        self.assertEqual(c_major_3, [48, 52, 55])

        c_major_5 = get_chord_notes("C", "maj", 5)
        self.assertEqual(c_major_5, [72, 76, 79])

    def test_get_chord_notes_invalid_chord(self):
        """Test invalid chord type handling"""
        with self.assertRaises(InvalidChordError):
            get_chord_notes("C", "invalid_type", 4)

    def test_get_chord_notes_invalid_root(self):
        """Test invalid chord root handling"""
        with self.assertRaises(InvalidNoteError):
            get_chord_notes("H", "maj", 4)

    def test_get_chord_frequencies(self):
        """Test chord frequency generation"""
        c_major_freq = get_chord_frequencies("C", "maj", 4)
        self.assertEqual(len(c_major_freq), 3)
        self.assertAlmostEqual(c_major_freq[0], 261.63, places=2)
        self.assertAlmostEqual(c_major_freq[1], 329.63, places=2)
        self.assertAlmostEqual(c_major_freq[2], 392.0, places=2)

    def test_get_chord_frequencies_with_rounding(self):
        """Test chord frequencies with custom rounding"""
        c_major_freq = get_chord_frequencies("C", "maj", 4, round_digits=4)
        self.assertTrue(all(isinstance(f, float) for f in c_major_freq))

    def test_get_chord_frequencies_inversion(self):
        """Test chord frequencies with inversion"""
        c_major_first_freq = get_chord_frequencies("C", "maj", 4, inversion=1)
        self.assertEqual(len(c_major_first_freq), 3)

    def test_get_chord_names(self):
        """Test chord type listing"""
        chord_names = get_chord_names()
        self.assertIn("maj", chord_names)
        self.assertIn("min", chord_names)
        self.assertIn("7", chord_names)
        self.assertIn("maj7", chord_names)
        self.assertIn("dim", chord_names)
        self.assertIn("aug", chord_names)


if __name__ == "__main__":
    unittest.main()
