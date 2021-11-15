# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. Külje pikkused ei pea olema täisarvud.
# (ujukomaarv - float)
num1 = float(input("Sisesta esimese külje pikkus: "))
num2 = float(input("Sisesta teise külje pikkus: "))
num3 = float(input("Sisesta kolmanda külje pikkus: "))

if num1 == num2 == num3:
    print("Kolmnurk on võrdkülgne.")
elif (num1 <= 0) or (num2 <= 0) or (num3 <= 0):
    print("Kolmnurk ei ole võimalik.")
elif num1 == num3:
    print("KOlmnurk on võrdhaarne.")
else:
    print("Kolmnurk on erikülgne.")