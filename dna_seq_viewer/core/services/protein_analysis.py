from collections import Counter


alphabet = 'AGLSVTKDINEPRFQYHCMW'


def aa_breakdown(sequence):
    c = Counter(sequence)
    length = len(sequence)
    for residue in c.keys():
        c[residue] = round((c[residue] / length) * 100, 2)
    return c
