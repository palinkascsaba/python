
def megfordito(string):
    for letter in string:
        sorszam = string.find(letter)
        megforditott_szo = ''
        uj_sorszam = -(sorszam + 1)
        uj_betu = string[uj_sorszam]
        megforditott_szo += uj_betu
        print(megforditott_szo)
megfordito("hello!")