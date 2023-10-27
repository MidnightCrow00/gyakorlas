def gyakorlas_1():
    i = 0
    while i < 151:
        print(i)
        i += 2

# for i in range(0,151,2):
#     print(i)

def gyakorlas_2():
    osztszam = 0
    listaszam = 0
    while not (listaszam == 10):
        listaszam += 1
        szam = int(input("Szam: "))
        if szam % 3 == 0:
            osztszam += 1
    print("Ennyi szám osztható 3-al: ", osztszam)

def gyakorlas_3():
    szam = int(input("Szam: "))
    while not (szam % 10 == 0):
        szam = int(input("Szam: "))
