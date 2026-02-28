"""Protein Translation"""

import textwrap


def proteins(strand):
    codons = textwrap.wrap(strand, 3)
    protein = []
    for codon in codons:
        if codon in ["AUG"]:
            protein.append("Methionine")
        elif codon in ["UUU", "UUC"]:
            protein.append("Phenylalanine")
        elif codon in ["UUA", "UUG","CUU", "CUC", "CUA", "CUG"]:
            protein.append("Leucine")
        elif codon in ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]:
            protein.append("Serine")
        elif codon in ["UAU", "UAC"]:
            protein.append("Tyrosine")
        elif codon in ["UGU", "UGC"]:
            protein.append("Cysteine")
        elif codon in ["UGG"]:
            protein.append("Tryptophan")
        if codon in ["UAA", "UAG", "UGA"]:
            break
    return protein
