import csv
def obtener_dato_csv(ruta_archivo, fila, columna):
    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        datos = list(lector_csv)
        dato = datos[fila][columna]
    return dato

def wallapopData(fila):
    email = obtener_dato_csv("Sites/wallapop.csv", fila, 0)
    password = obtener_dato_csv("Sites/wallapop.csv", fila, 1)
    title = obtener_dato_csv("Sites/wallapop.csv", fila , 2)
    price = obtener_dato_csv("Sites/wallapop.csv", fila, 3)
    currency = obtener_dato_csv("Sites/wallapop.csv", fila, 4)
    category = obtener_dato_csv("Sites/wallapop.csv", fila, 5)
    subcategory = obtener_dato_csv("Sites/wallapop.csv", fila, 6)
    specify = obtener_dato_csv("Sites/wallapop.csv", fila, 7)
    productState = obtener_dato_csv("Sites/wallapop.csv", fila, 8)
    description = obtener_dato_csv("Sites/wallapop.csv", fila, 9)
    hashtags = obtener_dato_csv("Sites/wallapop.csv", fila, 10)
    photoFolderPath = obtener_dato_csv("Sites/wallapop.csv", 1, 11)
    shipping = obtener_dato_csv("Sites/wallapop.csv", fila, 12)
    weight = obtener_dato_csv("Sites/wallapop.csv", fila, 13)
    return email, password, title, price, currency, category, subcategory, specify, productState, description, hashtags, photoFolderPath, shipping, weight
