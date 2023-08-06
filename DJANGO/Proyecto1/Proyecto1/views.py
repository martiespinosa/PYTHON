from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request): # primera funcion vista
    doc_externo = open(r"C:\Users\MARTI\Documents\Carpeta Principal\PYTHON\DJANGO\Proyecto1\Proyecto1\Plantillas\saludo.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()

    hola = plantilla.render(contexto)

    return HttpResponse(hola)


def despedida(request):
    return HttpResponse("Adiós mundo!")


# "%s" (marcador de posición)(muy util para poner una variable en medio de una constante)
def fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    fecha = """
    <h2>
    Fecha y hora actual %s 
    </h2>
    """ %(fecha_actual)

    return HttpResponse(fecha)


def calcular_edad(request, edad_actual, agno):
    # edad_actual = 20
    periodo = agno - 2023
    edad_futura = periodo + edad_actual
    respuesta = """
    <h3>
    En el año %s tendrás %s años
    </h3>
    """ %(agno, edad_futura)

    return HttpResponse(respuesta)
