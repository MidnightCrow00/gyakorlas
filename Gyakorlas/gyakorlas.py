def gyak_4():
    szam = int(input("Szam: "))
    while not (szam >= 10 and szam < 100 and szam % 2 == 0):
        szam = int(input("Szam: "))

def gyak_5():
    szam = int(input("Szam: "))
    while not (szam > 0 and szam % 2 == 1):
        szam = int(input("Szam: "))

def gyak_6():
    szam = float(input("Szam: "))
    while not (szam > 0 and int(szam ** 0.5) ** 2 == szam or szam % 3 == 0):
        szam = float(input("Szam: "))

def gyak_7():
    szam1 = float(input("Szam1: "))
    szam2 = float(input("Szam2: "))
    alap = float(input("Alap: "))
    osszeg = szam1 + szam2 + alap
    while not (osszeg > 0 and szam1 + szam2 > alap and alap + szam2 > szam1 and szam1 + alap > szam2):
        szam1 = float(input("Szam1: "))
        szam2 = float(input("Szam2: "))
        alap = float(input("Alap: "))
    print("Ezekből lehet háromszög")

def gyak_8():
    szoveg = input("3 betűs szöveg: ")
    while not (szoveg.isalpha() and len(szoveg) == 3):
        szoveg = input("3 betűs szöveg: ")
    print(szoveg.upper())

def gyak_9():
    szoveg = input("4 betűs szöveg: ")
    while not (szoveg.isalpha() and szoveg.islower() and len(szoveg) == 4):
        szoveg = input(" 4 betűs szöveg: ")

def gyak_10():
    osszeg = 0
    szam = float(input("Szam: "))
    szamlalo = 0

    while not (szam == 0):
        szamlalo += 1
        osszeg = osszeg + szam
        szam = float(input("Szam: "))

    atlag = osszeg / szamlalo
    print(f"Átlag {atlag:.2f}")

def gyak_11():
    #nincs kész
    osszeg = 0
    szam = float(input("Szam: "))
    szamlalo = 0

    while not (szam == 0):
        szamlalo += 1
        osszeg = osszeg + szam
        szam = float(input("Szam: "))

    atlag = osszeg / szamlalo
    print(f"Átlag {atlag:.2f}")