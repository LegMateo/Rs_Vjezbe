# ZADATAK 7
""" def Broj_i_slovo(a):
    state1, state2 = False, False
    for slovo in a:
        if slovo.isupper():
            state1 = True
        elif slovo.isdigit():
            state2 = True
    if state2 and state1 == True:
        return True
    else:
        return False


a = input("Unesi lozinku: ")

if len(a) < 8 or len(a) >= 18:
    print("Lozinka mora sadržavati između 8 i 15 znakova")
elif Broj_i_slovo(a) == False:
    print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
elif "password" in a.lower() or "lozinka" in a.lower():
    print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
else:
    print("Lozinka je jaka!")  """

# ZADATAK 8
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filtriraj_parne(lista):
    temp = []

    for broj in lista:
        if broj % 2 == 0:
            temp.append(broj)

    return temp


print(filtriraj_parne(lista)) """

# ZADATAK 9

"""
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def ukloni_duplikate(lista):
    jedinstveni = set(lista)

    return list(jedinstveni)


print(ukloni_duplikate(lista))  # [1, 2, 3, 4, 5] 

"""

# ZADATAK 10
"""
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

obj = {}


def brojanje_rijeci(tekst):
    rijeci = tekst.split()

    for rijec in rijeci:
        if rijec in obj:
            obj[rijec] += 1
        else:
            obj[rijec] = 1
    return obj


print(brojanje_rijeci(tekst))
"""

# ZADATAK 11

"""
def grupiraj_po_paritetu(lista):
    temp1, temp2 = [], []

    for broj in lista:
        if broj % 2 == 0:
            temp1.append(broj)
        else:
            temp2.append(broj)

    return {"parni": temp1, "neparni": temp2}


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
"""

# ZADATAK 12

"""
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}


def obrni_rjecnik(rijecnik):

    temp = {}

    for key, value in rjecnik.items():
        temp[value] = key  
    return temp


print(obrni_rjecnik(rjecnik))
# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}

"""

# ZADATAK 13
"""

def prvi_i_zadnji(lista):

    return (lista[0], lista[-1])


def maks_i_min(lista2):
    min = lista2[0]
    max = lista2[0]
    for num in lista2:
        if num > max:
            max = num
        elif num < min:
            min = num
    return max, min


def presjek(skup_1, skup_2):

    return skup_1 & skup_2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(prvi_i_zadnji(lista))  # (1, 10)

print(maks_i_min(lista2))  # (250, 5)

print(presjek(skup_1, skup_2))  # {4, 5}

"""

# ZADATAK 14

"""
def isPrime(num):

    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primes_in_range(start, end):

    result = []
    for i in range(start, end):
        if isPrime(i) == True:
            result.append(i)
    return result


print(isPrime(10))
print(primes_in_range(1, 10))  # [2, 3, 5, 7]

"""

# ZADATAK 15


def count_vowels_consonants(tekst):
    count_vowels = 0
    count_consonants = 0
    for znak in tekst:
        if znak in vowels:
            count_vowels += 1
        elif znak in consonants:
            count_consonants += 1

    return {"vowels": count_vowels, "consonants": count_consonants}


vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
# {'vowels': 30, 'consonants': 48}
