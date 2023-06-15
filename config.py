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
    photoFolderPath = obtener_dato_csv("Sites/wallapop.csv", fila, 11)
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
        #Recambios de coches y furgonetas
    if number == '2' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        #Recambios de motos y triciclos
    elif number == '2' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div/ul/li[5]'
    # Moda y accesorios
        #Abrigos y chaquetas
    elif number == '3' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        #Accesorios
    elif number == '3' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        #Bañadores
    elif number == '3' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Belleza y Cosmetica
    elif number == '3' and subcategoryNumber == '4':
        if specifyNumber == '1':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        #Bolsos, maletas y carteras
    elif number == '3' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif specifyNumber == '11':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        #Bufandas y guantes
    elif number == '3' and subcategoryNumber == '6':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Calzado
    elif number == '3' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        #Joyas
    elif number == '3' and subcategoryNumber == '9':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif specifyNumber == '11':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        #Prendas y vestidos
    elif number == '3' and subcategoryNumber == '10':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif specifyNumber == '11':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif specifyNumber == '12':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif specifyNumber == '13':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        elif specifyNumber == '14':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[14]'
        elif specifyNumber == '15':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[15]'
        elif specifyNumber == '16':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[16]'
        elif specifyNumber == '17':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[17]'
        elif specifyNumber == '18':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[18]'
        elif specifyNumber == '19':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[19]'
        elif specifyNumber == '20':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[20]'
        elif specifyNumber == '21':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[21]'
        elif specifyNumber == '22':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[22]'
        elif specifyNumber == '23':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[23]'
        elif specifyNumber == '24':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[24]'
        #Ropa deportiva
    elif number == '3' and subcategoryNumber == '11':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        #Ropa interior y calcetines
    elif number == '3' and subcategoryNumber == '12':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        #Sombreros
    elif number == '3' and subcategoryNumber == '14':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        #Trajes
    elif number == '3' and subcategoryNumber == '15':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        #Otros
    elif number == '3' and subcategoryNumber == '16':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
    # TV, audio y foto
        #Auriculares y cascos
    elif number == '4' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Cámaras y fotografia
    elif number == '4' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        #Pilas y cargadores
    elif number == '4' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Proyecteros y accesorios
    elif number == '4' and subcategoryNumber == '6':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Reproductores
    elif number == '4' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        #Televisores
    elif number == '4' and subcategoryNumber == '8':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        #Video
    elif number == '4' and subcategoryNumber == '9':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
    # Móviles y telefonía
        # Accesorios
    elif number == '5' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Piezas y recambios
    elif number == '5' and '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
    # Informática y Electrónica
    elif number == '6' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
    elif number == '6' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
    elif number == '6' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
    # Bicicletas
        # Accesorios
    elif number == '8' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Bicicletas
    elif number == '8' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        # Piezas
    elif number == '8' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        # Proteccion
    elif number == '8' and subcategoryNumber == '4':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
    # Hogar y jardin
        # Almacenaje
    elif number == '10' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        # Articulos para mascotas
    elif number == '10' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        # Baño
    elif number == '10' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        # Cocina
    elif number == '10' and subcategoryNumber == '4':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Colchon
    elif number == '10' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Decoración
    elif number == '10' and subcategoryNumber == '6':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        # Iluminacion
    elif number == '10' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Jardin
    elif number == '10' and subcategoryNumber == '8':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Mobiliario
    elif number == '10' and subcategoryNumber == '9':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
    # Cine, Libros y música
        # Cds y vinilos
    elif number == '12' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Equipo Profesional
    elif number == '12' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Instrumentos Musicales
    elif number == '12' and subcategoryNumber == '4':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        # Libros
    elif number == '12' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Peliculas
    elif number == '12' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
    # Niños y Bebés
        #Alimentacion
    elif number == '13' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Maternidad
    elif number == '13' and subcategoryNumber == '3':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        # Articulos Escolares
    elif number == '13' and subcategoryNumber == '4':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Cunas
    elif number == '13' and subcategoryNumber == '5':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        # Juguetes
    elif number == '13' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Ropa
    elif number == '13' and subcategoryNumber == '8':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        elif specifyNumber == '11':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[11]'
        elif specifyNumber == '12':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[12]'
        elif specifyNumber == '13':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[13]'
        # Seguridad
    elif number == '13' and subcategoryNumber == '9':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        # Bebe
    elif number == '13' and subcategoryNumber == '10':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        elif specifyNumber == '7':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[7]'
        elif specifyNumber == '8':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[8]'
        elif specifyNumber == '9':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[9]'
        elif specifyNumber == '10':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[10]'
        # Tronas
    elif number == '13' and subcategoryNumber == '11':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
    # Construcción y Reformas
        # Baños
    elif number == '15' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        # Herramientas
    elif number == '15' and subcategoryNumber == '7':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        # Pavimentos
    elif number == '15' and subcategoryNumber == '9':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        # Pinturas
    elif number == '15' and subcategoryNumber == '10':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        # Puertas y ventanas
    elif number == '15' and subcategoryNumber == '11':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
    # Industria y agricultura
        # Agricultura
    elif number == '16' and subcategoryNumber == '1':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'
        elif specifyNumber == '6':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[6]'
        # Industria
    elif number == '16' and subcategoryNumber == '2':
        if specifyNumber == '1':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[1]'
        elif specifyNumber == '2':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[2]'
        elif specifyNumber == '3':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[3]'
        elif specifyNumber == '4':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[4]'
        elif specifyNumber == '5':
            return '//*[@id="objectType2"]/div/tsl-dropdown-list/div/div[2]/ul/li[5]'






