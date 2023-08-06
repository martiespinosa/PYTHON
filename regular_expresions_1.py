import re

# texto = "Hola mundo, ejemplo de texto 1, ejemplo de texto 2, ejemplo de texto 3"
# textoBuscar = "mundo"
# textoEncontrado = re.search(textoBuscar, texto)

# print(textoEncontrado.start())
# print(textoEncontrado.end())
# print(textoEncontrado.span())




texto = "Hola mundo, ejemplo de texto 1, ejemplo de texto 2, ejemplo de texto 3"
textoBuscar = "texto"

print(len(re.findall(textoBuscar, texto)))


