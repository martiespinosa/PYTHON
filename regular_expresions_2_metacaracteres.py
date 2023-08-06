import re

lista_nombres = ['David Calle',
                 'Alvaro Díaz',
                 'Pedro Duque',
                 'Alvaro Molina',
                 'Olga Díaz',
                 'Alvaro García',
                 'Monica Díaz']

# metacaracter "^" (comienza por)
for i in lista_nombres:
    if re.findall('^Alvaro', i):
        print(i)

print("\n")

# metacaracter "$" (finaliza por)
for i in lista_nombres:
    if re.findall('Díaz$', i):
        print(i)

print("\n")

# metacaracter "[]" (Ctrl+F)(es como re.search)
for i in lista_nombres:
    if re.findall('[M]', i):
        print(i)

print("\n")

# ----------------------------------------------------------------

lista_random = ['hombres',
                 'mujeres',
                 'mascotas',
                 'niños',
                 'niñas',
                 'camión',
                 'camion']

# metacaracter "[]" (comodín)
for i in lista_random:
    if re.findall('niñ[oa]s', i):
        print(i)

print("\n")

# metacaracter "[]" (comodín)
for i in lista_random:
    if re.findall('cami[oó]n', i):
        print(i)




