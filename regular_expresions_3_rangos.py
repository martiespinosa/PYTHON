import re

# re.search mira si coincide
# re.match mira si coincide sólo al inicio

listaNombres = ['Ana',
                'Pedro',
                'María',
                'Rosa',
                'Sandra',
                'Celia',
                'Julia',
                'Lara',
                'Jara']

# metacaracter "[-]" (rango)(devuelve los nombres de lista que contengan de la A a la J (también se pude hacer con números))(en este caso que empiezan de la A a la J por el metacaracter "^" antes de "[-]")
for i in listaNombres:
    if re.findall('^[a-j]', i, re.IGNORECASE): # re.IGNORECASE para desactivar el case sensitive
        print(i)

print("\n")

# metacaracter comodín "." (Actúa como un caracter cualquiera)
for i in listaNombres:
    if re.findall('.ara', i):
        print(i)

print("\n")

# ----------------------- Patrones de búsqueda "\" -------------------------

listaRandom = ['Pedro',
               '574893',
               'a5u7y8']

# "\d" (digit)(que contiene números)(se puede combinar con "^" o "$" para quu contenga el número sólo al inicio o sólo al final)
for i in listaRandom:
    if re.findall('^\d', i):
        print(i)
