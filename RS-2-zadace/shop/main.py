from narudzbe import napravi_narudzbu, unesi_proizvode
from proizvodi import skladiste

proizvodi = unesi_proizvode()


narudzba = napravi_narudzbu(proizvodi, skladiste)


print(narudzba.ispis())
