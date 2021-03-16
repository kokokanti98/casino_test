from requests import get
from bs4 import BeautifulSoup
import datetime
import time
from os import system, name
from termcolor import colored
import winsound

url = "https://www.amazon.fr/dp/B08HBQWBHH/"  # le lien de la 3090
url2 = "https://www.amazon.fr/dp/B013M1QN9K/"  # le lien de card dispo

headers = {"USER-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.160"}


def availability():
    while True:
        page = get(url2, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        titre = soup.find(id="productTitle").get_text().strip()
        #print(titre.strip()) Nvidia Graphic Card K1200
        avaibility = soup.find(id="availability").get_text().strip()[0:31]
        #print(avaibility) #Il ne reste plus que 2 exemplaire(s) en stock.
        prix = soup.find(id="priceblock_ourprice")
        if(prix is None):
            prix = "0"
        else:
            prix = prix.get_text()
        #print(prix.strip()) 498,00 €
        if(avaibility == 'Voir les offres de ces vendeurs'):
            affichage(titre, avaibility, prix, "red")
            seconde = 60
            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")
            print(f"{now} prochaine actualisation dans {seconde} secondes...")
            time.sleep(seconde)
            continue
        else:
            affichage(titre, avaibility, prix, "green")
            jouerSon()
            break


def affichage(titre, availability, prix, color):
    clear()
    print(colored(titre + "\n " + availability + " \n" + prix, color))


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def jouerSon():
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)


availability()
