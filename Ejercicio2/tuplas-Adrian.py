'''
tupla= ("Jueves", 2, 3.5,(5,34),"amapola",False, None)
print(tupla)
lista = list(tupla)
lista[1] = 21
tupla = tuple(lista)
print(tupla)
tupla1 = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(tupla1)
lista1 = list(tupla1)
lista1[0]="Festivo"
tupla1=tuple(lista1)
print(tupla1)
'''
'''
t = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

print(t[::2])

if "Martes" in t:
    print("Esta dentro")
else:
    print("No esta")

if "Marzo" in t:
    print("Esta dentro")
else:
    print("No esta")
'''
'''
t1=("Z",)
t2=("z",)
t3=(t1+t2)*5
print(t3)
'''
'''
t = ("LUNES","MARTES","MIERCOLES","JUEVES","VIERNER","SABADO","DOMINGO")

dia=(input("Dime el dia que quieres comprobar: ")).upper()
if dia not in t:
    print("Ese dia no existe")
else:
    print(f"Ese dia es el indice {t.index(dia)} de la tupla y es el dia {t.index(dia)+1} de la semana")
'''
'''
t = (4,3,7,4,78)
print(t)
l = list(t)
l.sort()
t = tuple(l)
print(t)
'''




