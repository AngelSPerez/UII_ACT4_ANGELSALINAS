from django.shortcuts import render

def mostrar_datos(request):
    empleados = [
        {"nombre": "Ana López", "puesto": "Cajera", "edad": 28},
        {"nombre": "Carlos Ruiz", "puesto": "Gerente", "edad": 35},
        {"nombre": "María Torres", "puesto": "Almacén", "edad": 22}
    ]
    return render(request, "index.html", {"empleados": empleados})

