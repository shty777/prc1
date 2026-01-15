from dataclasses import dataclass
from typing import Literal

SeqKind = Literal["DNA", "RNA"]

@dataclass(frozen=True, slots=True)
class SeqStats:
    id: str
    kind: SeqKind
    length: int
    gc_fraction: float

from Sequences.Sequences import DNASequence, RNASequence
from Sequences.Sequences import NucleotideSequence


def summarise(seq: NucleotideSequence) -> SeqStats:

    if isinstance(seq, DNASequence):
        kind: SeqKind = "DNA"
    elif isinstance(seq, RNASequence):
        kind = "RNA"
    else:
        raise TypeError("Unsupported sequence type")

    return SeqStats(
        id=seq.id,
        kind=kind,
        length=len(seq.seq),
        gc_fraction=RNASequence.calc_gc_content(seq),
    )
