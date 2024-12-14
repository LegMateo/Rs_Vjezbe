# 1. Kvadriranje broja:
kvadriraj = lambda broj: broj**2

print(kvadriraj(2))

# 2. Zbroji pa kvadriraj:
zbroj_pa_kvadrat = lambda broj1, broj2: (broj1 + broj2) ** 2

print(zbroj_pa_kvadrat(1, 1))

# 3. Kvadriraj duljinu niza:
niz = [1, 2, 3, 4, 5]

kvadriraj_duljinu = lambda niz: len(niz) ** 2

print(kvadriraj_duljinu(niz))

# 4. Pomnoži vrijednost s 5 pa potenciraj na x:

mnozi_pa_potenciraj = lambda x, y: (x * y) ** 2

print(mnozi_pa_potenciraj(5, 5))

# 5. Vrati True ako je broj paran, inače vrati None:

is_paran = lambda broj: broj % 2 == 0

print(is_paran(3))
