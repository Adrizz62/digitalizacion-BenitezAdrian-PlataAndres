valido = False
longitud = 0
while valido == False:
    nombre = input("Dime le nombre del agente:").strip()
    apellido = input("Dime le apellido del agente:").strip()
    if nombre.isalpha() == True and apellido.isalpha() == True:
        valido = True
longitud = len(nombre)
if len(nombre) < len(apellido):
    longitud = len(apellido)
alias = nombre[:3].upper()+"-"+apellido[-3:].upper()+"-"+str(longitud)
print(alias)