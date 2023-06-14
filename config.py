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

def wallapopCategorySwitch(number):
    if number == '1':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
    elif number == '2':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
    elif number == '3':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
    elif number == '4':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
    elif number == '5':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
    elif number == '6':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
    elif number == '7':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
    elif number == '8':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
    elif number == '9':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
    elif number == '10':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
    elif number == '11':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
    elif number == '12':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
    elif number == '13':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
    elif number == '14':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
    elif number == '15':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
    elif number == '16':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
    elif number == '17':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[17]'
    elif number == '18':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[18]'
    elif number == '19':
        return '//*[@id="category"]/div/tsl-dropdown-list/div/div[2]/ul/li[19]/div'

def wallapopSubcategorySwitch(number, subcategoryNumber):
    #Motor y accesorios
    if number == '2':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
    #Moda y accesorios
    elif number == '3':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
        elif subcategoryNumber == '16':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
    #TV, audio y foto
    elif number == '4':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
    #Móviles y telefonía
    elif number == '5':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[8]'
    #Informática y Electrónica
    elif number == '6':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[8]'
    #Deporte y Ocio
    elif number == '7':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
    #Bicicletas
    elif number == '8':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
    #Consolas y videojuegos
    elif number == '9':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
    #Hogar y jardin
    elif number == '10':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
    # Electrodomésticos
    elif number == '11':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
    # Cine, Libros y música
    elif number == '12':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
    # Niños y Bebés
    elif number == '13':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
    # Coleccionismo
    elif number == '14':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
        elif subcategoryNumber == '16':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
    # Construcción y Reformas
    elif number == '15':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
    # Industria y agricultura
    elif number == '16':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'

def wallapopSpecifySwitch(number, subcategoryNumber, specifyNumber):
    # Motor y accesorios
    if number == '2':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
    # Moda y accesorios
    elif number == '3':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
        elif subcategoryNumber == '16':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
    # TV, audio y foto
    elif number == '4':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
    # Móviles y telefonía
    elif number == '5':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[8]'
    # Informática y Electrónica
    elif number == '6':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[8]'
    # Deporte y Ocio
    elif number == '7':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
    # Bicicletas
    elif number == '8':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
    # Consolas y videojuegos
    elif number == '9':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
    # Hogar y jardin
    elif number == '10':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
    # Electrodomésticos
    elif number == '11':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[7]'
    # Cine, Libros y música
    elif number == '12':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
    # Niños y Bebés
    elif number == '13':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
    # Coleccionismo
    elif number == '14':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif subcategoryNumber == '13':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif subcategoryNumber == '14':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif subcategoryNumber == '15':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
        elif subcategoryNumber == '16':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
    # Construcción y Reformas
    elif number == '15':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif subcategoryNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif subcategoryNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif subcategoryNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif subcategoryNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif subcategoryNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif subcategoryNumber == '8':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif subcategoryNumber == '9':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif subcategoryNumber == '10':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif subcategoryNumber == '11':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif subcategoryNumber == '12':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
    # Industria y agricultura
    elif number == '16':
        if subcategoryNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif subcategoryNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div/ul/li[2]'






