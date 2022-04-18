import json
from pickle import FALSE, TRUE
import requests
from bs4 import BeautifulSoup
import pandas as pd


nombre = str(input("Introduce un nombre: "))
var = 'https://www.minube.com/que_ver/espana/' + nombre

data = {}
data['QueVer'] = []


r = requests.get('https://www.minube.com/que_ver/espana/' + nombre)
soup = BeautifulSoup(r.content, 'html.parser')
pagina = soup.find_all("div", {"class": "display_table buttonMain"})

ultPag = pagina.pop(1)
paginaFinal = int(ultPag.get_text())
print(paginaFinal)
#Linea necesaria para reducir el tiempo de desarrollo BORRAR DESPUES
paginaFinal = 2

file = open('Scrappers\JSON\\'+ nombre+'.json', 'w', encoding='utf-8')

#Paginacion para la web
for pag in range(paginaFinal):
    print(pag)
    url = str(var) +'?page='+ str(pag)
    print(url)
    req = requests.get(url)
    soup3 = BeautifulSoup(req.content, 'html.parser')

    # Alternativa a find_all o find
    rows = soup.select(".itemsGrid a.titleItem")

    for row in rows:

        link = row.get('href')
        print("Link de la web: " + link + "\n")

        #Ingreso en cada URL
        re = requests.get(link)
        soup2 = BeautifulSoup(re.content, 'html.parser')

        #Obtencion de datos
        datosLugar = soup2.find_all("a", {"class": "data"})
        imagen = soup2.find("img", {"class": "picture"})
        opinion = soup2.find_all("div", {"class": "textContainer"})
        #URL siguiente, para paginacion


        if imagen == None:
            print("Sin imagenes")
        else:
            imagen = soup2.find("img", {"class": "picture"}).get('data-src')
            print(imagen)
            print("1---------------" + "\n")

        if datosLugar == None:
            print("Sin dirección")
        else:
            datosLugar = soup2.find_all("a", {"class": "data"})
            listaLugar = []
            for element in datosLugar:
                a = element.get_text()
                listaLugar.append(a)
                print(a)
            
            print("2---------------" + "\n")

        if opinion == None:
            print("Sin opinión")
        else:
            opinion = soup2.find_all("div", {"class": "textContainer"})
            listaOp = []
            for element in opinion:
                a = element.get_text()
                listaOp.append(a)
                print(a)
            
            print("3---------------" + "\n")
        
        data['QueVer'].append({
            'Url': link,
            'Foto': imagen,
            'Contacto': listaLugar,
            'Opinion': listaOp})

json.dump(data, file, indent=4)
    

# rows = soup.find_all("div", {"class": "riverItems"})
# rows = soup.find_all("a", {"class": "titleItem"})

# print(rows)


