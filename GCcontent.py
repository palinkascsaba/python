# File olvasása, sorok listába helyezése
def readFile(filePath):
    with open(filePath, 'r') as f:
        return[l.strip() for l in f.readlines()]  
#GC-kontent meghatározás
def gc_content(seq):
#Ha nincs semmi benne akkor 0-t ad ki error helyett.
    if len(seq) == 0:
        return 0.0
    return round((seq.count('C') + seq.count('G')) / len(seq)*100,6)

#FASTA fájl sorai listában, de szet vannak vagva sorok szerint, nehez vele dolgozni
FASTAfile = readFile(r"C:\Users\Csaba\Desktop\code\Rosalind\Stronghold\fastafileok\gc_content.txt")
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
#GC - contentet rendel hozzá a labelekhez
Resultdict = {key: gc_content(value) for (key, value) in FASTAdict.items()}
#megkeresi a legmagasabb GC-contentű stringet.
MaxGCKey = max(Resultdict, key=Resultdict.get)
#kinyomja ugy ahogy kell a rosalindnak
print(f'{MaxGCKey[1:]}\n{Resultdict[MaxGCKey]}')