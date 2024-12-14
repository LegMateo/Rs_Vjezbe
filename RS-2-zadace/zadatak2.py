# 1
nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda duljina: len(duljina) ** 2, nizovi))

print(kvadrirane_duljine)  # [36, 36, 36, 49]

# 2
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda broj: broj > 5, brojevi))

print(veci_od_5)  # [21, 33, 45, 9, 10]

# 3
brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda broj: (broj, broj**2), brojevi))

print(transform)  # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}


# 4
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 18},
    {"ime": "Iva", "prezime": "Ivić", "godine": 18},
    {"ime": "Mate", "prezime": "Matić", "godine": 1},
]
svi_punoljetni = all(list(map(lambda student: student["godine"] >= 18, studenti)))
print(svi_punoljetni)  # False

# 5
rijeci = [
    "jabuka",
    "pas",
    "knjiga",
    "zvijezda",
    "prijatelj",
    "zvuk",
    "čokolada",
    "ples",
    "pjesma",
    "otorinolaringolog",
]
min_duljina = input("Unesite minimalnu duljinu riječi: ")
# min_duljina = 7
duge_rijeci = list(filter(lambda rijec: len(rijec) > int(min_duljina), rijeci))
print(duge_rijeci)  # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
