'''
tupla= ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(tupla)
lista = list(tupla)
lista[1]= "Festivo"
tupla= tuple(lista)
print(tupla)
'''
'''
tupla= ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print (tupla[::2])
print("Martes" in tupla, "martes si esta dento de la tupla")
print("Marzo" in tupla, "Marzo no esta dentro de la tupla")
'''
'''
t1= ("Z",)
t2= ("z",)
print((t1+t2)*5)
'''
'''
i= input("Dime un dia de la semana: ").upper()

dia= ("LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO")
if dia.index(i) ==-1:
    print("No hay dia")
else:
    print(f"El dia {i} esta en el indice {dia.index(i)} ")
'''
'''
tupla= ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
dia= input("Dime el dia: ")
if dia not in tupla:
    print ("Error")
else:
    print("El indice es", tuple.index(dia))
'''