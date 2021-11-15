# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse
# while on korduslause, kui sa soovid midagi korrata, sa saad korrata seda kasutades: "while(True):"
# int teeb arvud täisarvuks (nt: 5), float teeb arvud ujukoma arvuks (nt: 5.0)- seetõttu, kui sa soovid täpsemaid numbreid ja komakohti, on hea mõte kasutada float'i
kroonid = input("Sisesta kroonid: ")
eur = float(kroonid) / 15.6466
print("Teisendatud summa on: ", round(eur, 2))