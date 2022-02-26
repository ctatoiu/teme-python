# 1. Ipotenuza triunghi dreptunghic (20p)

import math
catena1 = float(input("Lungime catena 1: "))
catena2 = float(input("Lungime catena 2: "))
ipotenuza = math.sqrt(catena1**2 + catena2**2)
print("Ipotenuza este: ", round(ipotenuza,2))

# 2. Convertor lungime (25p)

KM_PE_MILA = 1.61
km = float(input("Introduceti distanta in km: "))
miles=km/KM_PE_MILA
print("Distanta in mile: ", round(miles,3))
mile = float(input("Introduceti distanta in mile: "))
kms=mile*KM_PE_MILA
print("Distanta in kilometri: ", round(kms,3))

# 3. Conversie timp (30p, a/b=10/20)
# a) Cititi de la utilizator 3 numere intregi - h,m,s - care reprezinta impreuna lungimea unui interval de timp, exprimata in ore, minute si secunde. Calculati si tipariti lungimea acestui interval exprimata in milisecunde.


hours = int(input("Introduceti orele: "))
minutes = int(input("Introduceti minutele: "))
seconds = int(input("Introduceti secundele: "))
ms = (hours*60**2+minutes*60+seconds)*1000
print("Lungimea intervalului este: ", ms, "ms")

# b) Cititi de la utilizator un numar intreg, care reprezinta lungimea unui interval de timp exprimata in secunde. Convertiti aceasta valoare la un numar de ore, minute si secunde (cu valorile pentru minute si secunde in intervalul lor normal 0..59), si tipariti aceasta valoare, in formatul: h:m:s

secunde = int(input("Introduceti nr de secunde: "))
h = secunde//3600
m = (secunde%3600)//60
s = secunde - (h*3600) - (m*60)

# print("Lungimea intervalului este: ", h, "h", m, "m", s, "s")
# Mai sus am comentat si un output alternativ, am pastrat mai jos forma ceruta

print("Lungimea intervalului este: ", h, ":", m, ":", s)

# 4. Verificare ordine (15p)
# a) Cititi de la utilizator 2 numere si verificati daca sunt date in ordine crescatoare sau sunt egale, si afisati True in acest caz, altfel False

no1 = int(input("Introduceti nr 1: "))
no2 = int(input("Introduceti nr 2: "))
crescatoare = no2>=no1
print("Numerele sunt in ordine crescatosare sau egale: ", crescatoare)

# b) Cititi de la utilizator 3 numere (a,b,c), verificati daca sunt toate ordonate - toate strict crescator sau toate strict descrescator - si in oricare din aceste doua cazuri afisati True (altfel False)

numero1 = int(input("Introduceti nr 1: "))
numero2 = int(input("Introduceti nr 2: "))
numero3 = int(input("Introduceti nr 3: "))
up_or_down = numero1 > numero2 > numero3 or numero1 < numero2 < numero3
print("Cele 3 numere sunt ordonate strict?", up_or_down)

# 5. Aceeasi lungime (10p)
# Cititi de la utilizator 2 fragmente de text (ca valori de tip string), apoi afisati lungimea in caractere a fiecaruia, si de asemenea valoarea True daca au aceeasi lungime, sau False in caz contrar.

text1 = str(input("Introduceti primul text: "))
text2 = str(input("Introduceti al doilea text: "))
compare=len(text1)==len(text2)
print("Lungime texte: ", len(text1), len(text2), "Au aceeasi lungime: ", compare)