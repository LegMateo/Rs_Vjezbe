class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        return [
            f"naziv: {self.naziv}, cijena: {self.cijena}, kolicina: {self.dostupna_kolicina}"
        ]


proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100},
]


skladiste = [Proizvod("Banana", 2, 555), Proizvod("Salama", 3, 32)]


def dodaj_proizvod(skladiste, proizvodi_za_dodavanje):
    for artikl in proizvodi_za_dodavanje:
        skladiste.append(
            Proizvod(artikl["naziv"], artikl["cijena"], artikl["dostupna_kolicina"])
        )


a = dodaj_proizvod(skladiste, proizvodi_za_dodavanje)

for proizvod in skladiste:
    print(proizvod.ispis())
