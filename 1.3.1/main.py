import pygame, sys

from interne.Accueil.__init__ import carre_system, update_carre
pygame.init()
from interne.Gameplay.__init__ import entities, update

largeur, hauteur = 800, 600
fenetre =pygame.display.set_mode((largeur, hauteur))
clock =pygame.time.Clock()





first = True

def start_game():
    print("start_game")

def update_game():
    print("update_game")



states = {
    "accueil": {
        "init": carre_system,
        "update": update_carre
    },
    "game": {
        "init": start_game,
        "update": update_game
    }
}

def Restart(first, stats):
    first == True
    states[current_state]["init"](fenetre)

current_state, new_state = "accueil", "accueil"

pygame.mixer.init()  # initialise le module son

pygame.mixer.music.load("interne/music/game-music.MP3")  # chemin vers le fichier
pygame.mixer.music.play(-1)  # -1 = boucle infinie
pygame.mixer.music.set_volume(0.5)  # 0.0 (muet) à 1.0 (volume max)


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
    
    
    if new_state == "game" and current_state != new_state: 
        first = True
        print(current_state, new_state)
        current_state = new_state
            
    
    
    
    
    #print(current_state)
   
    if current_state == "game":
        
        if first == True:
            print("Gameplay lancée")
            entities(largeur,hauteur,fenetre)
            first = False
        else:
            update(fenetre,events, largeur, hauteur)

        
    if current_state == "quit":
        pygame.quit()
        sys.exit()
    
    
    
    
    pygame.display.update()
            
    
    
    
    
    
    
    