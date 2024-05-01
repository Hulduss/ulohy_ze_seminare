# libovolné zadané číslo ze převedou do zvolené číselné soustavy (2-62)
# autor: Aneta Huličová <hulicovaa@jirovcovka.net>

cislo = int
soustava = int

# definice funkce
def prevod_do_soustavy(cislo, soustava):
    """
    převod čísla na zadanou číselnou soustavu
    """
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

# hlavní program
cislo = int(input("Zadejte číslo k převodu: "))
soustava = int(input("Zadejte číselnou soustavu (2-62): "))

# zavolání fukce
result = prevod_do_soustavy(cislo, soustava)
print(result)