# -*- coding: utf-8 -*-
#======================================================================
# Autoroute_de_la_mort.py Prog_up 2021-03-30
#
# Projet : Autoroute de la mort
#======================================================================
from turtle import *
from dessin import voiture, game_over
from time import sleep
from random import randint, randrange

#======================================================================
# Classe Voiture

class Voiture:
    def __init__(self, hero, couleur) : #hero = booléen
        self.j = hero
        self.c = couleur

#======================================================================
# Actions du joueurs

def depl_g(end = False) :
    for v in route[4] :
        if v != None and v.j == True and route[4].index(v) != 0 and end == False and route[4][route[4].index(v) - 1] == None :
            garde = route[4].index(v)
            route[4][garde - 1] = v
            route[4][garde] = None
            afficher(route)
            end = True

def depl_d(end = False) :
    for v in route[4] :
        if v != None and v.j == True and route[4].index(v) != 2 and end == False and route[4][route[4].index(v) + 1] == None :
            garde = route[4].index(v)
            route[4][garde + 1] = v
            route[4][garde] = None
            afficher(route)
            end = True

#======================================================================
# Actions des ennemis

def spawn_ennemis() :
    def avec_issue(x, y = 1) :
        """Fonction vérifiant qu'il y a au moins une issue (un passage) pour le joueur, elle s'utilise au niveau de l'espace libre entre les ennemis"""
        if y == 2 or route[y][x] != None :
            return route[y][x] == None
        #Issue à Gauche
        elif x == 0 and route[y][0] == None :
            if route[y][1] == None :
                if route[y][2] == None :
                    return avec_issue(0, y + 1) and avec_issue(1, y + 1) and avec_issue(2, y + 1)
                return avec_issue(0, y + 1) and avec_issue(1, y + 1)
            return avec_issue(0, y + 1)
        #Issue au Millieu
        elif x == 1 and route[y][1] == None :
            if route[y][0] == None or route[y][2] == None :
                return avec_issue(0, y + 1) and (avec_issue(1, y + 1) or avec_issue(2, y + 1))
            return avec_issue(1, y + 1)
        #Issue à Droite
        elif x == 2 and route[y][2] == None :
            if route[y][1] == None :
                if route[y][0] == None :
                    return avec_issue(0, y + 1) and avec_issue(1, y + 1) and avec_issue(2, y + 1)
                return avec_issue(2, y + 1) and avec_issue(1, y + 1)
            return avec_issue(2, y + 1)
    end = False
    ennemi = Voiture(False, "red")
    while not end :
        res = randrange(7)
        if res == 0 :
            end = True
        elif res == 1 and avec_issue(1) and avec_issue(2) :
            route[0][0] = ennemi
            end = True
        elif res == 2 and avec_issue(1) and avec_issue(0) :
            route[0][2] = ennemi
            end = True
        elif res == 3 and avec_issue(2) and avec_issue(1) : #"and avec_issue(1)" permet de résoudre un bug provoquant un bouchon
            route[0][0] = ennemi
            route[0][1] = ennemi
            end = True
        elif res == 4 and avec_issue(0) and avec_issue(1) : #"and avec_issue(1)" permet de résoudre un bug provoquant un bouchon
            route[0][1] = ennemi
            route[0][2] = ennemi
            end = True
        elif res == 5 and avec_issue(1) :
            route[0][0] = ennemi
            route[0][2] = ennemi
            end = True
        elif res == 6 and (avec_issue(0) or avec_issue(2))  :
            route[0][1] = ennemi
            end = True

def depl_ennemis() :
    for ordonnee in range(4, -1, -1) :
        for abscisse in range(3) :
            if route[ordonnee][abscisse] != None and route[ordonnee][abscisse].j == False :
                reset()
                if ordonnee != 4 :
                    route[ordonnee + 1][abscisse] = Voiture(False, "red")
                    route[ordonnee][abscisse] = None
                else :
                    route[ordonnee][abscisse] = None

#======================================================================
# Affichage des voitures

def voiture_turtle(abscisse, ordonnee, hero, couleur) :
    up()
    if hero == True :
        setheading(0)
        goto(ordonnee * 200 - 230, abscisse * -50)
        down()
        voiture(couleur)
    else :
        setheading(180)
        goto(ordonnee * 200 - 180, abscisse * -150 + 500)
        down()
        voiture(couleur)

def afficher(m) :
    reset()
    for ordonnee in range(5) :
        for abscisse in range(3) :
            if m[ordonnee][abscisse] != None :
                voiture_turtle(ordonnee, abscisse, m[ordonnee][abscisse].j, m[ordonnee][abscisse].c)

#======================================================================
# Gestion dans le temps

def time_loop() :
    global score
    hero_present = False
    for abscisse in range(3) :
         if route[4][abscisse] != None and route[4][abscisse].j :
            hero_present = True
    if hero_present == False :
        game_over(score)
    else :
        spawn_ennemis()
        depl_ennemis()
        score += 1
        afficher(route)
    ontimer(time_loop, (2000//score) + 200)

#======================================================================
# Autoroute

route = [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
route[4][1] = Voiture(True, "yellow")
#======================================================================
# Score

score = 0
#======================================================================
# Jeu

if __name__ == "__main__" :
    listen()
    bgpic("fond_route.png")
    end = False
    tracer(False)
    afficher(route)
    time_loop()
    onkey(bye, 'Escape')
    onkey(depl_g, 'Left')
    onkey(depl_d, 'Right')
    update()
    mainloop()
    print("Autoroute_de_la_mort est OK")
