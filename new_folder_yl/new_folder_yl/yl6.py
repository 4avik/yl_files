# "Int" on kasutatud arvu teisendamiseks v. tõlkimiseks: Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)
x = int(input("Sisesta esimene arv (x): "))
y = int(input("Sisesta teine arv (y): "))
z = int(input("Sisesta kolmas arv (z): "))

if x > y and x > z:
    print("Suurem number on X: ", x)
elif y > x and y > z:
    print("Suurem number on Y: ", y)
elif z > x and z > y:
    print("Suurem number on Z: ", z)