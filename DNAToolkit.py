import random
Nucleotides = ['A', 'G', 'C', 'T']

#Random DNS szekvenciát gyárt
def sequence_randomizer(length):
    random_sequence =''
    for x in range(length):
        random_sequence += random.choice(Nucleotides)
    return random_sequence    


#DNS-szekvenciát validálja, hogy csak helyes nukleotidok vannak-e benne.
def validateSeq(dna_seq):
    upperseq = dna_seq.upper()
    for nucleotide in upperseq:
        if nucleotide not in Nucleotides:
            return False
    return upperseq

#Nukleotid gyakoriságot ad meg.
def Nucount(seq):
    freqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0,}
    for nucleotide in seq:
        freqDict[nucleotide] += 1
    return freqDict
