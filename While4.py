"""Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură."""
n=eval(input("dati un numar:"))
suma=0
produsul=1
nr=1
while n>=nr:
    suma+=nr
    produsul*=nr
    nr+=1 

print("suma=",suma)
print("produsul=",produsul)
print("media aritmetica=",suma/n)