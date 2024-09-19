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

#Gyorsabb, nincs annyi if statement (python specifikus de konnyebb)
def gyorsabb_komplementator(seq):
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

#GC arányt mér
def gc_content(seq):
#Ha nincs semmi benne akkor 0-t ad ki error helyett.
    if len(seq) == 0:
        return 0.0
    return round((seq.count('C') + seq.count('G')) / len(seq)*100,2)

#fájlt elolvassa, sorokként listázza
def readFile(filePath):
    with open(filePath, 'r') as f:
        return[l.strip() for l in f.readlines()]  
    
#fájlt elolvassa, sorokként listázza, dictionaryba-teszi key:label value:string,
def FASTAread(filePath):
    FASTAfile = readFile(filePath)
#egy dictionary a DNS stringnek és a labelnek, ebbe már egybe vannak a sorok
    FASTAdict = {}
#A pillanatnyi label-t ez tartalmazza
    FASTAlabel = ""
#Rendezi a FASTAdict-be az adatot, egysorossá teszi
    for line in FASTAfile:
        if ">" in line:
            FASTAlabel = line
            FASTAdict[FASTAlabel] = ""
        else:
            FASTAdict[FASTAlabel] += line
    return FASTAdict

#hamming distance-t számol 
def zip_hamming_distance(string_1,string_2):
    if len(string_1) != len(string_2):
        raise ValueError("Strings are not the same length")
    zipped_dna = zip(string_1,string_2)
    hammingdistance = [(nuc1,nuc2) for nuc1, nuc2 in zipped_dna if nuc1 != nuc2]
    return len(hammingdistance)