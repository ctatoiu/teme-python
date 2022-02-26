# 1. Verificare paritate (10p)
# Scrieti o functie par_impar(n) care primeste ca parametru un numar intreg si returneaza un rezultat de tip string, care contine una dintre valorile 'par'/'impar', in functie de paritatea numarului.
def par_impar(n):
    if n%2==0:
        print("par")
    else:
        print("impar")
par_impar(22)
# 2. Semn (15p)
# Scrieti o functie semn(n) care implementeaza functia semn din matematica, definita astfel: o functie care primeste ca parametru un numar si returneaza ca rezultat una din valorile: -1 daca numarul e negativ, +1 daca e pozitiv sau 0 daca e egal cu zero.
def semn(n):
    if n>0:
        print("1")
    elif n==0:
        print("0")
    else:
        print("-1")
semn(0)
# 3. Fizz Buzz (15p)
# Scrieti o functie fizzbuzz(n) care primeste ca parametru un numar intreg si afiseaza un text, bazat pe aceste reguli:
# daca numarul e divizibil cu 3, afiseaza 'fizz'
# daca numarul e divizibil cu 5, afiseaza 'buzz'
# daca numarul e divizibil si cu 3 si cu 5, afiseaza 'fizzbuzz'
# altfel afiseaza numarul initial
# Observatie: functia nu trebuie sa returneze nimic, doar sa afiseze valoarea
def fizzbuzz(n):
    if n%3==0 and n%5==0:
        print ("fizzbuzz")
    elif n%3==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    else:
        print(n)
fizzbuzz(15)
# 4. Cifra comuna (15p)
# Scrieti o functie numita cifra_comuna(x,y) care primeste ca parametrii 2 numere intregi si returneaza valoarea boolean True doar in cazul in care ambele numere au exact  2 cifre (sunt in intervalul 10..99) si au macar o cifra comuna, altfel returneaza valoarea False.
def cifra_comuna(x,y):

    if (x>9 and x<100 and y>9 and y<100) and (x%10==y%10 or x//10==y//10 or x%10==y//10 or y%10==x//10):
        print(True)
    else:
        print(False)
cifra_comuna(34,43)
# 5. Forma mai mare (20p: a/b=10)
# a) Scrieti o functie numita forma_mai_mare(raza,latura) care primeste ca parametrii 2 numere (posibil cu virgula) care reprezinta raza unui cerc si lungimea laturii unui  patrat, calculeaza ariile celor 2 forme si returneaza o valoare de tip string, una din variantele 'cerc' sau 'patrat', in functie de care forma avea aria mai mare.
from cmath import pi
def forma_mai_mare(raza, latura):
    arie_cerc=pi*raza**2
    arie_patrat=latura**2
    if arie_cerc>arie_patrat:
        print("cerc")
    else:
        print("patrat")
forma_mai_mare(10,20)
# b) Optional: scrieti o a doua versiune a metodei de mai sus, numita forma_clar_mai_mare, cu aceasta diferenta: daca  ariile celor doua forme sunt foarte apropiate ca valoare, adica daca diferenta lor (pozitiva sau negativa) e mai putin decat 1% din aria cercului, atunci va intoarce valoarea 'egale', altfel va intoarce 'cerc'/'patrat' dupa logica anterioara.
from cmath import pi
def forma_clar_mai_mare(raza, latura):
    arie_cerc=pi*raza**2
    arie_patrat=latura**2
    diferenta=arie_cerc-arie_patrat
    if abs(diferenta)*100/arie_cerc<1:
        print("egale")
    elif arie_cerc>arie_patrat:
        print("cerc")
    else:
        print("patrat")
forma_clar_mai_mare(10,5)
# 6. Verificare triunghi (25p: a=10,b=15)
# a) Scrieti o functie numita verifica_triunghi(a,b,c) care primeste ca parametrii 3 numere (posibil cu virgula) care reprezinta lungimile unor segmente, si verifica daca ele pot forma laturile unui triunghi sau nu, returnand unul din mesajele: 'triunghi valid' sau 'triunghi invalid'
# Nota: pentru a putea forma un triunghi valid, laturile trebuie sa respecte regula generala: 'lungimea oricarei laturi trebuie sa fie mai mica decat suma celorlalte doua' (si regula suplimentara: 'lungimea laturilor trebuie sa fie strict mai mare ca zero')
def verifica_triunghi(a,b,c):
    if a<b+c and b<a+c and c<a+b and a+b+c>0:
        print("triunghi valid")
    else:
        print("trinughi invalid")
verifica_triunghi(3, 4, 5)
# b) Optional: modificati functia anterioara astfel incat in cazul in care pot forma un triunghi valid, sa determine si tipul triunghiului, intorcand in loc de 'triunghi valid' una dintre valorile mai specifice:
# 'triunghi echilateral' (daca are toate laturile egale)
# 'triunghi dreptunghic' (pentru aceasta verificare puteti folosi teorema lui Pitagora in acest mod: daca patratul unei laturi este egal cu suma patratelor celorlalte doua laturi, atunci e dreptunghic...)
# 'triunghi oarecare' (pentru restul cazurilor)
def verifica_triunghi_2(a, b, c):
    if a<b+c and b<a+c and c<a+b and a+b+c>0 and a==b==c:
        print("Triunghi echilateral")
    elif a<b+c and b<a+c and c<a+b and a+b+c>0 and a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
        print("triunghi dretpinghic")
    elif a<b+c and b<a+c and c<a+b and a+b+c>0:
        print("triunghi oarecare")
    else:
        print("trinughi invalid")
verifica_triunghi_2(6, 4, 4)