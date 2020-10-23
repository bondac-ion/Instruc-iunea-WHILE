"""Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative.
 Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33."""
nr=0
suma_pozitiva=0
nr_pozitive=0
suma_negativa=0
nr_negative=0
media_pozitiva=0
media_negativa=0
n=1
while nr<=12 :
    n=eval(input('dati un numar:'))
    nr=nr+1
    if n>=0:
        nr_pozitive=nr_pozitive+1
        suma_pozitiva+=n
    else:
        nr_negative=nr_negative+1
        suma_negativa+=n

media_pozitiva=suma_pozitiva/nr_pozitive
print("media pozitiva=",round(media_pozitiva,2))
media_negativa=suma_negativa/nr_negative
print("media negativa=",round(media_negativa,2))
