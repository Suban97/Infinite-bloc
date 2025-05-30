def entities(largeur, hauteur, fenetre):
    from interne.Gameplay.User_Ennemis import User, tools, Mob, Score
    global Player, Ennemis, inst_score
    fenetre.fill((255,255,255))
    tools()

    Player = User(largeur, hauteur)
    Ennemis = Mob(largeur, hauteur)  # ← Instance unique
    inst_score = Score()
    
    print("User lancé")
    
    
    
    
    
    

def update(fenetre, events, largeur, hauteur):
    from interne.Gameplay.User_Ennemis import User, Mob, Game_over
    fenetre.fill((255,255,255))
    
    Player.Write_User(fenetre)
    Player.move(largeur, hauteur)
    
    new_state =Ennemis.update_spawn(fenetre, inst_score, Player, largeur, hauteur)
    #print(new_state)
    if new_state == "accueil":
        return new_state
    if new_state == "game":
        return new_state
    inst_score.affichage(fenetre,largeur, hauteur)
    inst_score.logic_lvl(Player, Ennemis, inst_score)
    
            