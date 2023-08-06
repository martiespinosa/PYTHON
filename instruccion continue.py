texto = "Texto de ejemplo"

contador = 0

for i in texto:

    if i == " ":
        continue
    contador += 1

print(contador)