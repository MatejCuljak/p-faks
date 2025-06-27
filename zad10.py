#Napisati rekurzivnu funkciju za Euklidov algoritam za pronalazak najvećeg zajedničkog djelitelja 2 broja
def euklidov_algoritam(a, b):
    if b == 0:
        return a
    else:
        return euklidov_algoritam(b, a % b)
    
#Napisati rekurzivnu funkciju za vraćanje elemenata Fibonaccijevog niza.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.
def ispis_obrnuto(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + ispis_obrnuto(s[:-1])
    
