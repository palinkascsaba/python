#komplement szálat készíti el.
def komplementator(sequence):
    forditatlan_komplement = ''
    komplement = ''
    for nucleotide in sequence: 
            if nucleotide == "A":
                komplement_bazis = "T"
            elif nucleotide == "T":
                komplement_bazis = "A"
            elif nucleotide == "G":
                komplement_bazis = "C"
            elif nucleotide == "C":
                komplement_bazis = "G"       
            forditatlan_komplement += komplement_bazis
    komplement = forditatlan_komplement[::-1]
    print (komplement)
    return komplement

sequence = 'GGCGGGTCGGCCTAACCAAGAGGTTAGGGCGGCATATACTTAACGATTGCAGCAAATATGCGAGTACACGATGCGTCTCCGCGTGTTCCCATTGTTAGAATATAGGAAATAGATGCTATGCGTAAAGTGTCTCACATCGGGCATCGGCGACAGAAGACTAAGTTAGTGGTGAGAGCGGCGGTGTACGTGATATTCCGAAAGCGTAGTCGCAATACAGGTATATAATATGCGGTGGCTTACTTGCACCCGGACGGACGGTATCATGATTTTACCTAAATGGGTTATACGTCCTTTAAAGGACGGCGCGCGCTGGGTTAATTGAGTTGTGCCCGATTTCCATATCGGATACAACTAAAAAACGGTTCAGACCCCTTCCAGGCCGTTGGCGAGGAGGGCTAGCTAGTACGGGGATCAGCTGTCAACCATAGCACCGGGGGCAAACCATCGAGGCCTCCTTTGATCAGCAACCGGCCCACCGCTCGAGGAACTCAGTAGCACGATTGGGCTTCCCTCAATTCGCTGGACGGGGAATCCCCTAGCGCAAGTGTGCAGTGACTTTTTATACTCGGTCTATCACCCAATTGCGAGGAAATAGAAGAAGACCAGGGCAACTGATGCCATTTTCGCCAACTAGTGTTGGTGGTGGTAAAACGTCGACAATAGGTCCACCGCCGCGCCCCTTGGCAGACTCAGCAGCTATTGCCTATTTCGGAGAACGAGTGTAGCTTTAAAGATCGTCTAGACATTCACCCCACGGCTACTTGCATTTCGGGGGGCTACACGACCCAGGTTAACGAGTATGGAGCGGTCCGTTTCGGCCTAACAAGGTTTGCCACCGGGTCTCTGAATAGCACACCGGTTTGACGCCCAGTAGCACGCCCTATAGGCCCCTCCGTGTCCCCACGCCCCGAGACAGAAGTGGTCAATGAGTACCGATAGAGGCCCTCTGTCTTCGAAAGATCACATTCTATTGCA'
komplementator(sequence)