from supabase import create_client
import json

url = "https://secxumjiywgzbfdwafsc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlY3h1bWppeXdnemJmZHdhZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1MDc4MjgsImV4cCI6MjAxMjA4MzgyOH0.wJUWAsPsIVZoba2OSRAPXUJmexJRjz0t7dSyyxPPDmw"

supabase = create_client(url, key)

#para listar los datos de una tabla:
table_name = input("Introduce el nombre de la tabla a modificar: \n -tag \n -calendars \n -comments \n -events \n -users \n ")

#Hace una consulta de la tabla seleccionada:
response = supabase.table(table_name).select("*").execute()