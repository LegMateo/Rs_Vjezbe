a, b = 0, 0

a = float(input("Unesi neku vrijdnost: "))
b = float(input("Unesi neku vrijdnost: "))

c = input("Unesi neku operator: ")

dozvoljeni = ("+", "-", "*", "%")

if c not in dozvoljeni:
    print("Greska")

if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "*":
    print(a * b)
if c == "/" and a or b != 0:
    print(a / b)
else:
    print("Nema dijeljenja s 0!")
