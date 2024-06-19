seznam_1="2 kg kruha"

veliki_seznam=["2 kg kruha","6 pomaranč", "8 jabolk", 123,True,-2]

print(veliki_seznam)

seznam=["Pes-Francoski Bulldog","Mali Martin",2]

verizni_seznam=[
    ["Pes-belgijski ovčar","Ace",4],
    ["Pes-Francoski Bulldog","Martin",5],
    seznam
]
print(veliki_seznam[0])
print(veliki_seznam[2])
print(veliki_seznam[2][2])

seznam[-1]
seznam[2]
"""
1. napiši seznam, ki ima vsaj 5 elementov
2. izpiši vsak element na 2 različna načina
"""

print(verizni_seznam[1][1])


for i in range(6):
    print(veliki_seznam[i])




veliki_seznam.append("Briketi za mačko")
print(veliki_seznam)
spr=veliki_seznam.pop(0)
print(veliki_seznam.pop(0))
print(veliki_seznam.pop(1))
print(veliki_seznam.pop(2))
print(veliki_seznam)
print(spr)

print(veliki_seznam)
veliki_seznam.remove(1)
print(veliki_seznam)


#Krajša naloga
# naredi primer seznama ki vsebuje sezname
# izpiši 3 poljubne elemente

"""
Daljša naloga:
Napiši seznam_ocen v katerega z uporabo input in zank apendiraj vse svoje zaključne ocene (funkcija append)
primer prej: seznam_ocen=[]             primer po appendiranju: seznam_ocen=[2,3,4,5,4,3,2,3]

nato izračunajte končno povprečje tako, da seštejete vse ocene iz seznama in jih delite z številom vseh ocen

"""

#Dodatna
# napiši seznam z vsaj 10 elementi 
# izpiši vsak element iz seznama v pravilnem vrstnem redu
# izpiši vsak element iz seznama v nasprotnem vrstnem redu
"""
predmeti=["mat","slo", "tja","bio","kem","špo"]
vseOcene=[]
for i in predmeti:
    vseOcene.append(int(input(f"Koliko imaš {i}?")))
seštevek=0
for i in vseOcene:
    seštevek=+1
print(seštevek/6)
"""
a=[1,2,3,4,5,6]
for i in a:
    print(i)
for i in a:
    print(a[-len(a)+i])