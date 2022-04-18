

from cgitb import html
from contextlib import suppress
from bs4 import BeautifulSoup
import requests
import os
from io import open
import firebase_admin
from firebase_admin import credentials,firestore

counter_dictionary = {}


def comunidadesmenu():

  linpagA="https://www.minube.com/a/subloc/p/63/all"
  pagina = requests.get(linpagA)
  soup = BeautifulSoup(pagina.content, 'html.parser')
  enlaces=[]
  i=1

  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCard"):

    enlaces.append(poblacion.find("a",class_="titleItem")['href'])
    prtpob=poblacion.find("a",class_="titleItem").getText()
    print(i , prtpob)
    i=i+1



  return enlaces










def poblacionesnube(comm):

  pagina = requests.get(comm)
  soup = BeautifulSoup(pagina.content, 'html.parser')


  apartado=soup.find("div", class_="title link")

  if apartado==None:
    final=listapoblacpocas(comm)
  else:
    final=listapoblaciones(apartado.get('onclick').split("'")[1])


  return final

def listapoblacpocas(comm):
  pagina = requests.get(comm)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  enlaces=[]
  i=1



  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCardlargeCard"):

    enlaces.append(poblacion.find("a",class_="titleItem")['href'])
    prtpob=poblacion.find("a",class_="titleItem").getText()
    print(i , prtpob)
    i=i+1



  return enlaces



def listapoblaciones(url):
  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  enlaces=[]
  i=1



  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCard"):

    enlaces.append(poblacion.find("a",class_="titleItem")['href'])
    prtpob=poblacion.find("a",class_="titleItem").getText()
    print(i , prtpob)
    i=i+1



  return enlaces


def mostrarcosas(url):

  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  nuevaurl=soup.find("a",class_="link")['href']

  pagina = requests.get(nuevaurl)
  soup2 = BeautifulSoup(pagina.content, 'html.parser')



  for link in soup2.find_all("a",class_="link"):
    print(link.get("href"))
    pagina3 = requests.get(link.get("href"))
    soup3 = BeautifulSoup(pagina3.content, 'html.parser')

    for element in soup3.find_all("a", class_="titleItem"):

      prtpob=element.getText()
      print(prtpob)

    linkcomp = soup2.findAll("a", class_="next button")

    siguiente=linkcomp[0].get("href")

    if type(siguiente) == None :
      siguiente="out"

  linkcomp = soup2.findAll("a", class_="next button")
  if len(linkcomp) != 0 :
    siguiente=linkcomp[0].get("href")
  else:
    siguiente="out"

  while(siguiente!="out"):


    #itemsGrid

    pagina2 = requests.get(siguiente)
    soup2 = BeautifulSoup(pagina2.content, 'html.parser')

    for element in soup2.find_all("a",class_="titleItem"):

     print(element.getText())

    linkcomp = soup2.findAll("a", class_="next button")
    if len(linkcomp) != 0 :
      siguiente=linkcomp[0].get("href")
    else:
      siguiente="out"


















commenu=comunidadesmenu()
eleccion = int(input())-1




lst=poblacionesnube(commenu[eleccion])


eleccion = int(input())-1


mostrarcosas(lst[eleccion])

print("Fin")

