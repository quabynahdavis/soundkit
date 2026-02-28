import unittest
from soundkit.core.scales import (
    get_scale_notes,
    get_scale_frequencies,
    get_scale_names,
)
from soundkit.exceptions import InvalidScaleError, InvalidNoteError


class TestScales(unittest.TestCase):

    def test_get_scale_notes_major(self):
        """Test major scale generation"""
        c_major = get_scale_notes("C", "major", 4)
        expected = [60, 62, 64, 65, 67, 69, 71]  # C4 to B4
        self.assertEqual(c_major, expected)

        g_major = get_scale_notes("G", "major", 4)
        expected_g = [67, 69, 71, 72, 74, 76, 77]  # G4 to F#5
        self.assertEqual(g_major, expected_g)

    def test_get_scale_notes_minor(self):
        """Test minor scale generation"""
        a_minor = get_scale_notes("A", "minor", 4)
        expected = [69, 71, 72, 74, 76, 77, 79]  # A4 to G5
        self.assertEqual(a_minor, expected)

        c_minor = get_scale_notes("C", "natural_minor", 4)
        expected_c = [60, 62, 63, 65, 67, 68, 70]  # C4 to Bb4
        self.assertEqual(c_minor, expected_c)

    def test_get_scale_notes_multiple_octaves(self):
        """Test multi-octave scale generation"""
        c_major_2oct = get_scale_notes("C", "major", 4, 2)
        expected_length = 14  # 7 notes per octave × 2 octaves
        self.assertEqual(len(c_major_2oct), expected_length)

        # Check that it spans two octaves
        self.assertEqual(c_major_2oct[0], 60)  # C4
        self.assertEqual(c_major_2oct[7], 72)  # C5
        self.assertEqual(c_major_2oct[13], 83)  # B5

    def test_get_scale_notes_pentatonic(self):
        """Test pentatonic scale generation"""
        c_pentatonic_major = get_scale_notes("C", "pentatonic_major", 4)
        expected = [60, 62, 64, 67, 69]  # C, D, E, G, A
        self.assertEqual(c_pentatonic_major, expected)

        a_pentatonic_minor = get_scale_notes("A", "pentatonic_minor", 4)
        expected_a = [69, 72, 74, 76, 79]  # A, C, D, E, G
        self.assertEqual(a_pentatonic_minor, expected_a)

    def test_get_scale_notes_blues(self):
        """Test blues scale generation"""
        c_blues = get_scale_notes("C", "blues", 4)
        expected = [60, 63, 65, 66, 67, 70]  # C, Eb, F, Gb, G, Bb
        self.assertEqual(c_blues, expected)

    def test_get_scale_notes_modes(self):
        """Test musical modes"""
        # Dorian mode
        d_dorian = get_scale_notes("D", "dorian", 4)
        expected_dorian = [62, 64, 65, 67, 69, 71, 72]  # D to C
        self.assertEqual(d_dorian, expected_dorian)

        # Mixolydian mode
        g_mixolydian = get_scale_notes("G", "mixolydian", 4)
        expected_mix = [67, 69, 71, 72, 74, 76, 77]  # G to F
        self.assertEqual(g_mixolydian, expected_mix)

    def test_get_scale_notes_invalid_scale(self):
        """Test invalid scale type handling"""
        with self.assertRaises(InvalidScaleError):
            get_scale_notes("C", "invalid_scale", 4)

    def test_get_scale_notes_invalid_root(self):
        """Test invalid scale root handling"""
        with self.assertRaises(InvalidNoteError):
            get_scale_notes("H", "major", 4)

    def test_get_scale_frequencies(self):
        """Test scale frequency generation"""
        c_major_freq = get_scale_frequencies("C", "major", 4)
        self.assertEqual(len(c_major_freq), 7)
        self.assertAlmostEqual(c_major_freq[0], 261.63, places=2)  # C4
        self.assertAlmostEqual(c_major_freq[6], 493.88, places=2)  # B4

    def test_get_scale_frequencies_multiple_octaves(self):
        """Test multi-octave scale frequencies"""
        c_major_2oct_freq = get_scale_frequencies("C", "major", 4, 2)
        self.assertEqual(len(c_major_2oct_freq), 14)

    def test_get_scale_frequencies_with_rounding(self):
        """Test scale frequencies with custom rounding"""
        c_major_freq = get_scale_frequencies("C", "major", 4, round_digits=4)
        self.assertTrue(all(isinstance(f, float) for f in c_major_freq))

    def test_get_scale_names(self):
        """Test scale type listing"""
        scale_names = get_scale_names()
        self.assertIn("major", scale_names)
        self.assertIn("minor", scale_names)
        self.assertIn("pentatonic_major", scale_names)
        self.assertIn("blues", scale_names)
        self.assertIn("dorian", scale_names)
        self.assertIn("mixolydian", scale_names)


if __name__ == "__main__":
    unittest.main()
