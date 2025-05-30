import pygame, sys
import os

from interne.Accueil.__init__ import carre_system, update_carre
pygame.init()
from interne.Gameplay.__init__ import entities, update

largeur, hauteur = 800, 600
fenetre =pygame.display.set_mode((largeur, hauteur))
clock =pygame.time.Clock()

music_path = os.path.join(os.path.dirname(__file__), "interne", "music", "game-music.mp3")
pygame.mixer.music.load(music_path)  # chemin vers le fichier
pygame.mixer.music.set_volume(0.5)  # 0.0 (muet) à 1.0 (volume max)

first = True

states = {
    "accueil": {
        "init": carre_system,
        "update": update_carre
    },
    "game": {
        "init": entities,
        "update": update
    },
    "settings" :{
        "init": None,  # A définir si nécessaire
        "update": None  # A définir si nécessaire
    }
}

pygame.mixer.music.play(-1)  # -1 = boucle infinie
current_state, new_state = "accueil", "accueil"
while True:
    clock.tick(60)
    
    events = pygame.event.get()
    for event in events :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    if current_state == "accueil":
        if first == True:
            states[current_state]["init"](fenetre)
            first = False
        else:
            new_state =states[current_state]["update"](fenetre, events, first, current_state)
            #print(new_state)
    
    
    
    if new_state == "game": 
        first = True
        print(" ancien et nouveau",current_state, new_state)
        current_state = new_state
        new_state = None
    if new_state == "accueil":
        first = True
        print(" ancien et nouveau",current_state, new_state)
        current_state = new_state
        new_state = None
    
    
    #print(current_state)
   
    if current_state == "game":
        if first == True:
            #print("Gameplay lancée")
            states[current_state]["init"](largeur, hauteur, fenetre)
            first = False
            
        else:
            new_state = states[current_state]["update"](fenetre, events, largeur, hauteur)
            #print("retour new", new_state)


        
    if current_state == "quit":
        pygame.quit()
        sys.exit()
    
    
    
    
    pygame.display.update()







