#Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo
# prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
import re
def provjeri_string():
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")

    if not ime or not prezime:
        print("Ime i prezime ne smiju biti prazni.")
        return

    prvo_slovo_ime = ime[0].lower()
    prvo_slovo_prezime = prezime[0].lower()

    pattern = rf"^{prvo_slovo_ime}.*\d[0-5].*{prvo_slovo_prezime}$"
    
    unos = input("Unesite string za provjeru: ")
    
    if re.match(pattern, unos):
        print("String je valjan.")
    else:
        print("String nije valjan.")

if __name__ == "__main__":
    provjeri_string()
