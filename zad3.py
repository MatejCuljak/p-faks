# Iz
# podataka
# učitanih
# u
# prethodnom
# primjeru
# sortirati
# listu
# Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.
# Nedovoljan
# 0-49%
# Dovoljan
# 50-65%
# Dobar
# 65-80%
# Vrlodobar
# 80-90%
# Izvrstan
# 90-100%

def sortiraj_ocjene(ocjene):
    ocjene.sort()
    return ocjene

def rang_ocjena(ocjene):
    rang = {
        "Nedovoljan": 0,
        "Dovoljan": 0,
        "Dobar": 0,
        "Vrlodobar": 0,
        "Izvrstan": 0
    }
    
    for ocjena in ocjene:
        if ocjena < 50:
            rang["Nedovoljan"] += 1
        elif ocjena < 65:
            rang["Dovoljan"] += 1
        elif ocjena < 80:
            rang["Dobar"] += 1
        elif ocjena < 90:
            rang["Vrlodobar"] += 1
        else:
            rang["Izvrstan"] += 1
            
    return rang
def main():
    ocjene = []
    while True:
        unos = input("Unesite ocjenu (ili 'kraj' za završetak): ")
        if unos.lower() == 'kraj':
            break
        try:
            ocjena = int(unos)
            if 0 <= ocjena <= 100:
                ocjene.append(ocjena)
            else:
                print("Ocjena mora biti između 0 i 100.")
        except ValueError:
            print("Molimo unesite ispravnu ocjenu.")
    
    if ocjene:
        sortirane_ocjene = sortiraj_ocjene(ocjene)
        print("Sortirane ocjene:", sortirane_ocjene)
        
        rang = rang_ocjena(sortirane_ocjene)
        print("Rang ocjena:", rang)
    else:
        print("Nema unesenih ocjena.")
if __name__ == "__main__":
    main()
