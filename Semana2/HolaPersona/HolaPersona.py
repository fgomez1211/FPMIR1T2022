

from datetime import datetime


NombrePersona = input("Por favor ingrese su nombre:")

print("Hola, te envio un saludo", NombrePersona, "en la fecha:", datetime.today().strftime("%Y-%M-%d"))

