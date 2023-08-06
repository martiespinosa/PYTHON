# Las funciones decorador reciben por parametro otra funcion y dentro tienen otra funcion que es la que devuelven

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs): # "*args" (numero indefinido de argumentos), "**kwargs" (argumentos con clave valor)
        # Acciones adicionales que decoran
        print("\nVamos a realizar un cálculo:")

        funcion_parametro(*args, **kwargs) # "*args" (numero indefinido de argumentos), "**kwargs" (argumentos con clave valor)

        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior


@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)


@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)


@funcion_decoradora
def potencia(base,exponente):   
    print(pow(base, exponente))


suma(10,10)
resta(15,5)
potencia(base=5,exponente=3)