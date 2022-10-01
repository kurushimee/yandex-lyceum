from functools import total_ordering

N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = [
    "прима",
    "секунда",
    "терция",
    "кварта",
    "квинта",
    "секста",
    "септима",
]


@total_ordering
class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def get_interval(self, other):
        return INTERVALS[
            abs(PITCHES.index(self.note) - PITCHES.index(other.note))
        ]

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[PITCHES.index(self.note)]
        return self.note

    def __eq__(self, other):
        return self.note == other.note

    def __lt__(self, other):
        return PITCHES.index(self.note) < PITCHES.index(other.note)

    def __lshift__(self, shift):
        shift = PITCHES.index(self.note) - shift
        while abs(shift) > N:
            shift += N
        return Note(PITCHES[shift], self.is_long)

    def __rshift__(self, shift):
        shift = PITCHES.index(self.note) + shift
        while shift >= N:
            shift -= N
        return Note(PITCHES[shift], self.is_long)
