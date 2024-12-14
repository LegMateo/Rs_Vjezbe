from proizvodi import skladiste


class Narudzba:
    def __init__(self, naruceni_proizvodi):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = sum(
            proizvod["cijena"] * proizvod["narucena_kolicina"]
            for proizvod in naruceni_proizvodi
        )

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join(
            f"{proizvod['naziv']} x {proizvod['narucena_kolicina']}"
            for proizvod in self.naruceni_proizvodi
        )
        return f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} EUR"


def napravi_narudzbu(proizvodi):
    naruceni_proizvodi = []
    for artikl in proizvodi:
        found = False
        for proizvod in skladiste:
            if proizvod.naziv == artikl["naziv"]:
                print(f"Proizvod {artikl['naziv']} je dostupan!")
                naruceni_proizvodi.append(
                    {
                        "naziv": proizvod.naziv,
                        "cijena": proizvod.cijena,
                        "narucena_kolicina": artikl["narucena_kolicina"],
                    }
                )
                found = True
                break
        if not found:
            print(f"Proizvod {artikl['naziv']} nije u prodaji!")

    return Narudzba(naruceni_proizvodi)


def unesi_proizvode():
    proizvodi = []
    print("Unesite ime proizvoda i količinu")
    print("Kad završite unesite `stop`")

    while True:
        proizvod = input("Unesite ime proizvoda: ")
        if proizvod.lower() == "stop":
            break
        kolicina = int(input("Unesite količinu: "))
        proizvodi.append({"naziv": proizvod, "narucena_kolicina": kolicina})

    return proizvodi


narudzbe = []
proizvodi = unesi_proizvode()
narudzba = napravi_narudzbu(proizvodi)
narudzbe.append(
    {"narudzba": narudzba.naruceni_proizvodi, "ukupna_cijena": narudzba.ukupna_cijena}
)

print(narudzba.ispis_narudzbe())
