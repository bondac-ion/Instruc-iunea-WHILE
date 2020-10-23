"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.  
Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12."""  

suma=0
n=1
while n%2!=0 and n%3!=0 :
    n=eval(input("dati un numar:"))
    while n%2==0:
        suma+=n
        n=eval(input("dati un numar:"))

print("suma=",suma)
    