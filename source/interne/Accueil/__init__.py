

def carre_system(fenetre):
    from interne.Accueil.animation import carre_function
    fenetre.fill((150, 150, 190))
    #Animation
    print("__init__ carre system")
    carre_function()
    
    from interne.Accueil.Affichage import tools
    #Affichage
    tools(fenetre)




def update_carre(fenetre, events, first, current_state):
    from interne.Accueil.animation import spawn_carre, move_carre
    fenetre.fill((150, 150, 190))
    move_carre(fenetre)
    
    from interne.Accueil.Affichage import button_select, affichage
    
    for event in events:
        new_state = button_select(event, first, current_state)
        #print(new_state)
        if new_state == "game":
            print("new = game")
            return new_state
    affichage(fenetre)
    
    
    
    
    
    