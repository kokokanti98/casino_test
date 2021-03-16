#import tp_casino.py
from tp_casino import Joueur
from tp_casino import Casino
from tp_casino import getArgentMise
from tp_casino import getNumeroMise

j1 = Joueur("The Mike", 2000)
c1 = Casino("Casa Blanca", j1)

def test_create_user():
    assert j1 != None, "le joueur n'a pas été crée"
    

def test_argent_positif():
    assert j1.argent >= 0, "l'argent de l'utilisateur est  négatif "


def test_creer_casino():
    assert j1 != None, "le casino n'a pas de joueur"
    assert c1 != None, "le casino n'a pas été crée "

def test_argent_mise():

    argentMise = 1
    argentMise = getArgentMise(argentMise, j1)
    assert argentMise >= 0,"Argent mise négatif !"
    assert argentMise <= j1.argent, "Argent misé superieur à l'argent du joueur !"
    

def test_numero_mise():
    numeroMise = 1
    numeroMise = getNumeroMise(numeroMise)
    assert numeroMise <= 49, "Numero mise en dehors de l intervalle 0-49 ! /Supérieur à 49"
    assert numeroMise >= 0, "Numero mise en dehors de l intervalle 0-49 ! /Négatif"
