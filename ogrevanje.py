"""
denar=input("Koliko denarja imaš? ")
denar=int(denar)
print("Imaš", denar, "€.")

cena_kruha=5
cena_mleka=2

print("Kruh stane ",cena_kruha,"€, mleko pa ",cena_mleka ,"€.")
print("grem v trgovino...")
print("kupil bom 1 mleko")
denar=denar-cena_mleka # denar- 2= nova vrednost denarja 
print("Ostalo mi je", denar, "€.")



if denar>cena_kruha:
    print("Kupim še kruh.")
    denar=denar-cena_kruha
    print("Ostalo mi je", denar, "€.")
elif denar>3:
    print("imam dovol denarja še za en sok če ga hočem:)")
else:
    print("Ne morem kupiti kruha ker nimam dovolj denarja."  )

"""


# if pogoj:
    # koda, ki se izvede, če je pogoj izpolnjen pogoj=True
# else:
    # koda, ki se izvede, če pogoj ni izpolnjen pogoj=False


# if pogoj:
    # koda, ki se izvede, če je pogoj izpolnjen pogoj=True
# elif pogoj2:
    # koda, ki se izvede, če je pogoj2 izpolnjen pogoj2=True
# else:
    # koda, ki se izvede, če pogoj ni izpolnjen pogoj=False in pogoj2=False













"""
napiši podoben program kot smo ga napisali skupaj
apmapk uporabbi druge artikle/izdelke in cene (npr. mango, pomaranča, čokolada, ...) (cena= npr 1,2,3,4,5,6,7,8,9)
z uporabo if stavkov preveri ali lahko kupiš izdelek ali ne
če lahko izdelek kupiš, ga tudi kupi in obvesti uporabnika o vsem dogajanju

"""

"""
napiši program ki simulira nakupovanje v spletni trgovini
uporabnik naj vnese količino denarja ki ga ima (uporabi input in casting!)
nato naj izmed 3 poljubnih izdelkov izbere 1 izdelek (preko input) in vnese količino tega izdelka
program naj izpiše ali vse izdelke lahko kupi ali ne
 če jih lahko naj izpiše koliko denarja mu je ostalo
 in se mu ponudi izbira ponovno če pa ne pa naj izpiše koliko denarja mu manjka

"""

"""
naredi konzolno igrico kjer uporabnik ugiba število med 1 in 100
program naj uporabnika obvesti ali je število preveliko ali premajhno
in ga prosi da ugiba naprej dokler ne ugotovi števila


import random
from random import randint

import random

def igra():
    skrito_stevilo = random.randint(1, 100)
    ugibanja = 0

    print("Pozdravljen v igri Ugani število!")
    print("Ugani število med 1 in 100.")

    while True:
        ugibanje = int(input("Tvoj ugib: "))
        ugibanja += 1

        if ugibanje < skrito_stevilo:
            print("Ugibano število je premajhno. Poskusi znova!")
        elif ugibanje > skrito_stevilo:
            print("Ugibano število je preveliko. Poskusi znova!")
        else:
            print("Čestitamo! Uganili ste število {} v {} poskusih!".format(skrito_stevilo, ugibanja))

            
            break

igra()
"""
import random
from random import randint


class Character:
    def __init__(self):
        self.ime = ""
        self.life = 100
        self.max_life = 100

    def napadi(self, sovraznik):
        napad = randint(0, 10)
        if napad == 0:
            print("Napad ni uspel! :(")
        else:
            print(f"{self.ime} napade {sovraznik.ime} in mu odstrani {napad} življenja.")
            sovraznik.life = sovraznik.life - napad

class Nasprotnik(Character):
    def __init__(self):
        super().__init__()
        self.ime = random(["Goblin", "Ork", "Troll", "Zmaj", "Vilinec"])
        self.life = randint(10, 50)

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.ime = input("Vnesi ime svojega junaka: ")
        self.life = 100
        self.max_life = 100
    
    def zdravi(self):
        zdravljenje = randint(0, 10)
        self.life = self.life + zdravljenje
        if self.life > self.max_life:
            self.life = self.max_life
        print(f"{self.ime} se je pozdravil za {zdravljenje} življenja.")

    def bitka(self, sovraznik):
        print(f"{self.ime} se bori proti {sovraznik.ime}.")
        while self.life > 0 and sovraznik.life > 0:
            self.napadi(sovraznik)
            if sovraznik.life > 0:
                sovraznik.napadi(self)

        if self.life > 0:
            print(f"{self.ime} je zmagal!")
        else:
            print(f"{sovraznik.ime} je zmagal!")
