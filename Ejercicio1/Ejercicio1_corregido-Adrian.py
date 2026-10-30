tranquilo = 0
susto = 0
maldito=0
total_fantasmas=0
valido = True
num_habitaciones=int(input("Dime cuantas habitaciones hay: "))
if num_habitaciones <0:
    valido = False
while valido == False :
    print("numero de habitaciones no valido")
    num_habitaciones=int(input("Dime cuantas habitaciones hay: "))
    if num_habitaciones>=0:
        valido = True
for i in range(num_habitaciones):
    num_fantasmas = int(input(f"Dime cuantos fantasmas hay en la habitacion {i+1}"))
    if num_fantasmas<0:
        valido=False
    while valido==False:
        print("numero de fantasmas no valido")
        num_fantasmas = int(input(f"Dime cuantos fantasmas hay en la habitacion {i+1}"))
        if num_fantasmas >=0:
            valido = True
    total_fantasmas += num_fantasmas
    if num_fantasmas==0:
        tranquilo += 1
        print("La habitacion esta tranquila")
    elif num_fantasmas>=1 and num_fantasmas <=3:
        susto += 1
        print("Susto")
    elif num_fantasmas>3:
        maldito +=1
        print("Habitacion maldita")
print(f"En la mansion hay {tranquilo} habitaciones tranquilas, hay {susto} habitaciones de susto y {maldito} habitaciones malditas")
print(f"El numero total de fantasmas es {total_fantasmas} y por habitacion hay una media de {total_fantasmas/num_habitaciones}fantasmas")
