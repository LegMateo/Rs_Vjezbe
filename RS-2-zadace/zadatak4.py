# 1
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, km):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.km = km

    def ispis(self):
        return f"Marka je: {self.marka}, model je: {self.model}, godina je: {self.godina_proizvodnje}, kilometraza je: {self.km}"


auto = Automobil("VW", "Polo", 2016, 100000)

# print(auto.model)
print(auto.ispis())


# 2
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroji(self):
        return self.a + self.b

    def oduzmi(self):
        return self.a - self.b

    def pomnozi(self):
        return self.a * self.b

    def podijeli(self):
        return self.a / self.b


brojevi = Kalkulator(1, 6)

print(brojevi.podijeli())


# 3
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def print(self):
        return f" ime: {self.ime}, prezime: {self.prezime}, godine: {self.godine}, ocjene: {self.ocjene}"

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)


studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]},
]

studenti_objekti = [
    Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    for student in studenti
]


print(studenti_objekti)


for student in studenti_objekti:
    print(student.print())
    print(student.prosjek())


najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())

print(
    f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, prosjek: {najbolji_student.prosjek()}"
)


# 4
class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * self.r * 3.14

    def povrsina(self):
        return self.r**2 * 3.14


krug = Krug(4)

print(f"Povrsina je {krug.povrsina()}, a opseg je {krug.opseg()}")


# 5
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        return f"Radim na poziciji {self.pozicija} i imam placu {self.placa}"


radnik1 = Radnik("Marko", "Intern", 1100)


print(radnik1.work())


class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"

    def give_raise(self, radnik, povecanje):
        radnik.placa = radnik.placa + povecanje
        return "Uspijesno povecana placa"


manager = Manager("Ivek", "Senior", "2000", "ICT")
print(manager.give_raise(radnik1, 400))

print(radnik1.work())
