# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvuta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 	22 + 222 = 246). Ära kasuta korrutamistehet. Ülesanne on lahendatav ainult liitmise operaatorit kasuades.
n1 = input("Sisesta täisarv vahemikus 1-9: ")

n2 = n1 + n1
n3 = n1 + n1 + n1

s = int(n1) + int(n2) + int(n3)
print(n1, n2, n3, s)