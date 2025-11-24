import math
from typing import List, Union
from ..exceptions import InvalidFrequencyError
from ..constants import CONCERT_PITCH


def frequency_to_cents(freq1: float, freq2: float) -> float:
    """Convert frequency ratio to cents."""
    if freq1 <= 0 or freq2 <= 0:
        raise InvalidFrequencyError("Frequencies must be positive")
    return 1200 * math.log2(freq2 / freq1)


def cents_to_ratio(cents: float) -> float:
    """Convert cents to frequency ratio."""
    return 2 ** (cents / 1200)


def ratio_to_cents(ratio: float) -> float:
    """Convert frequency ratio to cents."""
    if ratio <= 0:
        raise InvalidFrequencyError("Ratio must be positive")
    return 1200 * math.log2(ratio)


def semitones_to_ratio(semitones: float) -> float:
    """Convert semitones to frequency ratio."""
    return 2 ** (semitones / 12)


def ratio_to_semitones(ratio: float) -> float:
    """Convert frequency ratio to semitones."""
    if ratio <= 0:
        raise InvalidFrequencyError("Ratio must be positive")
    return 12 * math.log2(ratio)


def normalize_frequency(frequency: float, reference: float = CONCERT_PITCH) -> float:
    """Normalize frequency to the nearest reference pitch."""
    if frequency <= 0:
        raise InvalidFrequencyError("Frequency must be positive")

    # Find the nearest A note frequency and calculate the difference in cents
    nearest_a = reference * (2 ** (round(12 * math.log2(frequency / reference) / 12)))
    return nearest_a
