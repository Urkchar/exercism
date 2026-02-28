"""Protein Translation"""

import more_itertools


def proteins(strand):
    codons = more_itertools.chunked(strand, 3)
    TRANSLATION_TABLE = {
        "AUG" : "Methionine",
        "UUU" : "Phenylalanine",
        "UUC" : "Phenylalanine",
        "UUA" : "Leucine",
        "UUG" : "Leucine",
        "CUU" : "Leucine",
        "CUC" : "Leucine",
        "CUA" : "Leucine",
        "CUG" : "Leucine",
        "UCU" : "Serine",
        "UCC" : "Serine",
        "UCA" : "Serine",
        "UCG" : "Serine",
        "AGU" : "Serine",
        "AGC" : "Serine",
        "UAU" : "Tyrosine",
        "UAC" : "Tyrosine",
        "UGU" : "Cysteine",
        "UGC" : "Cysteine",
        "UGG" : "Tryptophan"
    }
    protein = []
    for codon in codons:
        codon = "".join(codon)
        if codon in TRANSLATION_TABLE:
            protein.append(TRANSLATION_TABLE[codon])
        else:
            break
    return protein
