from supabase import create_client
import json

url = "https://secxumjiywgzbfdwafsc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlY3h1bWppeXdnemJmZHdhZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1MDc4MjgsImV4cCI6MjAxMjA4MzgyOH0.wJUWAsPsIVZoba2OSRAPXUJmexJRjz0t7dSyyxPPDmw"

supabase = create_client(url, key)

#para listar los datos de una tabla:
table_name = input("Introduce el nombre de la tabla a modificar: \n -tag \n -calendars \n -comments \n -events \n -users \n ")

#Hace una consulta de la tabla seleccionada:
response = supabase.table(table_name).select("*").execute()

#Carga el nombre de los campos que obtiene mediante la API de Supabase
campos = list(json.loads(response.model_dump_json())["data"][0].keys())
campoIndividual = ""
for x in range(len(campos)):
    campoIndividual += "-"+campos[x]+"\n"

print('Esta es la lista de los campos en: '+table_name)
print(campoIndividual)

#Restringe al usuario poder modificar campos de forma erronea
while True:
    idName = input("Escribe el nombre del campo Id: ")
    if idName is None :
        print(f"'{idName}' no es un campo válido para la tabla. Por favor, ingresa un campo válido.")
        continue

    idNumber = int(input("Escribe la Id: "))
    if idNumber < 0:
        print("La Id debe ser un número entero positivo. Inténtalo de nuevo.")
        continue

    camposelect = input("Escribe el nombre del campo: ")
    if camposelect not in campos:
        print(f"'{camposelect}' no es un campo válido para la tabla. Por favor, ingresa un campo válido.")
        continue

    valueinsert = input("Inserta el valor que deseas insertar: ")

    response = supabase.table(table_name).update({camposelect: valueinsert}).eq(idName, idNumber).execute()

# Añadimos el ejercicio 2 para unificarlo todo en el mismo archivo 
while buscando:
    tabla = input('En que tabla quieres introducir los datos? \n - users \n - events \n - calendars \n - comments \n - tag \n')
    for campoTabla in listaTablas:
        
        if tabla.lower() == campoTabla:
            buscando = False

    if buscando != False:
        print("No se encontro la tabla, corrige si esta mal escrito")

response = supabase.table(tabla).select("*").execute()

datos = {}
