class SoundKitError(Exception):
    """Base exception for all SoundKit errors"""
    pass

class InvalidNoteError(SoundKitError):
    """Raised when Invalid note name is provided """
    pass

class InvalidOctaveError(SoundKitError):
    """Raised when octave is out of valid range"""
    pass

class InvalidFrequencyError(SoundKitError):
    """Raised when invalid frequency is provided"""
    pass

class InvalidChordError(SoundKitError):
    """Raised when invalid chord type is provided"""
    pass

class InvalidScaleError(SoundKitError):
    """Raised when invalid scale type is provided"""
    pass