import pygame, sys




def tools(fenetre):
    global font, TitreFont, buttons, selected
    print("tool")
    font =pygame.font.SysFont("Arial",36)
    TitreFont =pygame.font.SysFont("Comic Sans MS", 100)

    
    buttons =[("▶ JOUER", 250), ("⚙ OPTIONS", 330), ("✖ QUITTER", 410)] 
    selected =0
    
    fenetre.fill((150, 150, 190))




        

def button_select(event, first, current_state):
    global selected
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            selected = (selected + 1) % len(buttons)
        elif event.key == pygame.K_UP:
            selected = (selected - 1) % len(buttons)
        elif event.key == pygame.K_RETURN:
            if selected == 0:
                print("return game")
                return "game"
                first = True
            elif selected == 1:
                    print("Afficher les options")
            elif selected == 2:
                    pygame.quit()
                    sys.exit()
    

def affichage(fenetre):
    Titre =TitreFont.render("Infinite Bloc", True, (0, 0, 30))
    fenetre.blit(Titre, (100, 50))
    
    for i, (text, y) in enumerate(buttons):
            if i == selected: color = (0,0,0)
            else: color =(255,255,255)
            Label = font.render(text, True, color)
            rect = Label.get_rect(center=(400, y))
            fenetre.blit(Label, rect)
    

    