"""Protein Translation"""

import more_itertools

TRANSLATION_TABLE = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "AGU": "Serine",
    "AGC": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}


def proteins(strand):
    codons = more_itertools.chunked(strand, 3)
    protein = []
    for codon in codons:
        codon = "".join(codon)
        if codon not in TRANSLATION_TABLE:
            break
        protein.append(TRANSLATION_TABLE[codon])
    return protein
