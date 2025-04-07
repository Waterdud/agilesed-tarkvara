class Arstid:
    def __init__(self, nimi, vanus, eriala):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = []

class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus

class Haigla:
    def patsiendideKuuvamine(self, patsiendiList):
        for index, elem in enumerate(patsiendiList):
            print("ID: ", index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus)

    def arstideKuuvamine(self, arstidList):
        for index, elem in enumerate(arstidList):
            print("ID: ", index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus, "Eriala: ", elem.eriala)

    def kohtumineTegimene(self, arstideList):
        for arst in arstideList:
            if len(arst.aeg) > 0:
                print(f"Arstil {arst.nimi} on kohtumised ajaks: {arst.aeg}")
            else:
                print(f"Arstil {arst.nimi} ei ole kohtumisi.")

Patsient1 = Patsient("Dima", 18)
Patsient2 = Patsient("Eska", 17)
Patsient3 = Patsient("Janika", 17)

patsiendiList = [Patsient1, Patsient2, Patsient3]

Arst1 = Arstid("Vova genii", 85, "Hambaarst")
Arst2 = Arstid("Serega doter", 52, "Ortopeed")

ArstidList = [Arst1, Arst2]

haigla = Haigla()

haigla.patsiendideKuuvamine(patsiendiList)
print()
haigla.arstideKuuvamine(ArstidList)
print()
haigla.kohtumineTegimene(ArstidList)
