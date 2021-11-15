# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. 
# (sõne - string)
name = input("Mis su nimi on?: ")
print("Tere ", name, "!", sep='')

location = input("Kus sa elad?: ")
if location == "Saaremaal":
    print("Jälle need saarlased...")

age = int(input("Kui vana sa oled?: "))
if age < 18:
    print("Sa oled liiga noor, et autot juhtida! :(")
elif age == 18:
    print("Õnnitlused täisealiseks saamisel! >:D")
elif age > 18:
    print("Sa oled piisavalt vana, et autoga sõita! :)")

# elif location !=  "Saaremaal" or "Saaremaa":
#    print(":)")
