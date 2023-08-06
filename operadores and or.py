print("PROGRAMA DE BECAS")

distancia = int(input("Entra que tienes hasta el centro en km: "))
hermanos = int(input("Entra el número de hermanos que tienes: "))
salario_familia = int(input("Entra el salario anual de tu família: "))

if distancia > 40 and hermanos > 2 or salario_familia <= 20000:
    print("Eres apto para la beca")
else:
    print("No eres apto para la beca")
