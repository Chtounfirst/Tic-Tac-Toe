# grille = {
#     "A":[None,None,None],
#     "B":[None,None,None],
#     "C":[None,None,None]
# }
# """le dictionnaire contient la grille du jeu
#     """
# Joueurs = ["X","O"]
    
# def afficher_grille (grille)->dict:
#     print ("  1","  2","  3")
#     print("_____________")
#     for cle in grille:
#         print(cle,end="")
                
#         for elt in grille[cle]:        
            
#             if elt==None:
#                 print ("|","","|",end="")
#             else :
#                 print ("|",elt,"|",end="")
#         print("\n")
#     print(":::::::::::::")
            
#     """fonction d'affichage de la grille
#     """
   
# afficher_grille(grille)

# def verifier_si_le_coup_est_possible (grille)->bool:
       
#     jeu1=input("coup?:")

#     if int(jeu1[1]) in [1,2,3] and jeu1[0] in ["A","B","C"]:
#         print("test")   
#     if grille[jeu1[0]][int(jeu1[1])-1]==None:
#         print("test1")     
#     if grille[jeu1[0]][int(jeu1[1])-1]=="X":
#         print ("cette case est deja jouée")                
#     if grille[jeu1[0]][int(jeu1[1])-1]=="O":
#         print ("cette case est deja jouée")
#     return (jeu1)



# def coup_joueur (grille,coup,Joueurs)->bool:
#     coup=input("coup ?:")
#     for coup in grille[coup[0]][int[1]] == Joueurs:
#         if coup in grille
#             del grille["None"] == Joueurs 
#         else :
#             print ("pas possible")
#     return (Joueurs)

        
board = [" "," "," "," "," "," "," "," "," "]  
#defini le plateau du jeu
def afficher_plateau():
    print(board[0]+" | "+ board[1] + "|" + board[2])
    print("---------")
    print(board[3]+" | "+ board[4] + "|" + board[5])
    print("---------")
    print(board[6]+" | "+ board[7] + "|" + board[8])
    print("---------")
#verifier les coups gagnants  
def check_win():
    if (board[0]== board[1]==board[2] and board[0] != " ") or \
        (board[3]== board[4]==board[5] and board[3] != " ") or \
        (board[6]== board[7]==board[8] and board[6] != " ") or \
        (board[0]== board[3]==board[6] and board[0] != " ") or \
        (board[1]== board[4]==board[7] and board[1] != " ") or \
        (board[2]== board[5]==board[8] and board[2] != " ") or \
        (board[0]== board[4]==board[8] and board[0] != " ") or \
        (board[2]== board[4]==board[6] and board[2] != " "):
        return True
    else :
        return False
# jeu
player = "X"
game_over = False
while not game_over :
    afficher_plateau()
    move = input("player "+ player + ",tapez un chiffre de 1 à 9:")
    move = int(move) -1
    if board[move] == " ":
        board[move] = player
        if check_win():
            afficher_plateau()
            print("Player"+player+"win!")
            game_over = True
        elif " " not in board:
            afficher_plateau()
            print("hors jeu")
            game_over = True
        else :
            if player =="X":
                player ="O"
            else:
                player = "X"
else:
    print("case deja prise")
    
                        

    

    
    
    
      

          
            