# Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
# Prebrojati u rječnik koliko ima kojih ocjena.
# Izračunati postotak prolaznosti. (sve ocjene veće od 1)

import random
def generiraj_ocjene(ime_prezimena):
    ocjene = {}
    for ime in ime_prezimena:
        ocjena = random.randint(1, 5)
        ocjene[ime] = ocjena
    return ocjene
def prebroj_ocjene(ocjene):
    broj_ocjena = {i: 0 for i in range(1, 6)}
    for ocjena in ocjene.values():
        broj_ocjena[ocjena] += 1
    return broj_ocjena
def izracunaj_prolaznost(broj_ocjena):
    prolazne_ocjene = sum(broj_ocjena[i] for i in range(2, 6))
    ukupno_ocjena = sum(broj_ocjena.values())
    if ukupno_ocjena == 0:
        return 0
    return (prolazne_ocjene / ukupno_ocjena) * 100
def main():
    ime_prezimena = ["Petar Petric", "Ana Anic", "Marko Markovic", "Ivana Ivic", "Luka Lukic"]
    ocjene = generiraj_ocjene(ime_prezimena)
    print("Generirane ocjene:", ocjene)
    
    broj_ocjena = prebroj_ocjene(ocjene)
    print("Broj ocjena:", broj_ocjena)
    
    prolaznost = izracunaj_prolaznost(broj_ocjena)
    print(f"Postotak prolaznosti: {prolaznost:.2f}%")
if __name__ == "__main__":
    main()
