# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). (muutuja - variable, tingimus - condition, if-lause - if statement)
# variable, condition, if statement
# How to write a program that finds the minimum of a number inserted by a user

a = input("Sisesta arv: ")
b = input("Sisesta teine arv: ")

if a < b:
    print("Miinimum on:", a)
else:
    print("Miinumum on:", b)