#nukleotidokat szamol es konyvtarba rendezi
def Nucount(seq):
    freqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0,}
    for nucleotide in seq:
        freqDict[nucleotide] += 1
    return freqDict

szekvencia = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
result = Nucount(szekvencia)
#kiszedi csak az értékeket ' ' el elválasztva a formátum miatt.
print(' '.join([str(val) for key, val in result.items()]))