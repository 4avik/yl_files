# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.
# "!=" on eitus
# enne vaadatakse "and" tehet, alles siis "or" tehet. Tehete tegemise järjekorda saab sulgudega muuta.
x = int(input("Sisesta positiivne täisarv: "))

if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print("Tegu on liigaastaga.")

else:
    print("Tegu pole liigaastaga.")