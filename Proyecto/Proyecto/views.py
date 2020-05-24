from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):  # primera vista

    nombre = "Diego"

    doc_externo = open(
        "C:/Users/User/Documents/GitHub/proyectosDjango/Proyecto/Proyecto/plantillas/plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": nombre})

    documento = plt.render(ctx)

    return HttpResponse(documento)


def despedida(request):

    return HttpResponse("Hasta luego")


def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
        <body>
        <h1>
        Fecha y Hora actual %s
        </h1>
        </body>
        </html>""" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, agno):

    #edadActual = 18
    periodo = agno-2020
    edadFutura = edad+periodo
    documento = """<html>
        <body>
        <h2>
        En el año %s vas a tener %s años
        </h1>
        </body>
        </html>""" % (agno, edadFutura)

    return HttpResponse(documento)
