import pygame, sys

from interne.Accueil.__init__ import carre_system, update_carre
pygame.init()


size = 800, 600
fenetre =pygame.display.set_mode(size)
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
            carre_system(fenetre)
            first = False
        else:
            new_state =update_carre(fenetre, events, first, current_state)
            print(new_state)
    
    
    if new_state == "game":
        print(current_state, new_state)
        current_state = new_state
            
    
    
    
    
    #print(current_state)
   
    if current_state == "game":
        print("jeux")
    if current_state == "quit":
        pygame.quit()
        sys.exit()
    
    
    
    
    pygame.display.update()
            
    
    
    
    
    
    
    