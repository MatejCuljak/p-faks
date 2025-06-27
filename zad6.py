#Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
# Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
# imena + prezime.
# X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
# iprezime@sum.ba).
# Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
# Istražiti greedy i non-greedy quantifiers.
import re
def provjeri_email(email):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    return re.match(pattern, email) is not None
def provjeri_eduid(eduid):
    pattern = r'^[a-zA-Z]\w*X?@sum\.ba$'
    return re.match(pattern, eduid) is not None
def main():
    email = input("Unesite e-mail")
    eduid = input("Unesite eduId")
    if provjeri_email(email):
        print("E-mail je ispravan.")
    else:
        print("E-mail nije ispravan.")
    if provjeri_eduid(eduid):
        print("EduId je ispravan.")
    else:
        print("EduId nije ispravan.")
if __name__ == "__main__":
    main()

