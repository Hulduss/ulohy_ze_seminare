def prevod_do_soustavy(cislo, soustava):
    abeceda = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    vysledek = ""
    minus = False
    
    if cislo < 0:
        cislo = -cislo
        minus = True
        
    while cislo > 0:
        zbytek = cislo % soustava
        vysledek = abeceda[zbytek] + vysledek
        cislo //= soustava
        
    if minus:
        vysledek = "-" + vysledek
        
    return vysledek

cislo = int(input("Zadejte číslo k převodu: "))
soustava = int(input("Zadejte číselnou soustavu (2-62): "))


result = prevod_do_soustavy(cislo, soustava)
print(result)