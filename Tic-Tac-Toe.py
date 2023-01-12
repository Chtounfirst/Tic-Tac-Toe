grille = {
    "A":[None,None,None],
    "B":[None,None,None],
    "C":[None,None,None]
}
"""le dictionnaire contient la grille du jeu
    """
    
def afficher_grille (grille)->dict:
    print ("  1","  2","  3")
    print("_____________")
    for cle in grille:
        print(cle,end="")
                
        for elt in grille[cle]:        
            
            if elt==None:
                print ("|","","|",end="")
            else :
                print ("|",elt,"|",end="")
        print("\n")
    print(":::::::::::::")
            
    """fonction d'affichage de la grille
    """
   
afficher_grille(grille)

def verifier_si_le_coup_est_possible (grille)->bool:
       
    jeu1=input("coup?:")

    if int(jeu1[1]) in [1,2,3] and jeu1[0] in ["A","B","C"]:
        print("test")   
    if grille[jeu1[0]][int(jeu1[1])-1]==None:
        print("test1")     
    if grille[jeu1[0]][int(jeu1[1])-1]=="X":
        print ("cette case est deja jouée")                
    if grille[jeu1[0]][int(jeu1[1])-1]=="O":
        print ("cette case est deja jouée")
    return (jeu1)



def coup_joueur (grille,coup,joueur)->bool:
    coup=input("coup ?:")
    for coup in grille[coup[0]][int[1]]== jeu1:
        
        

    

    
    
    
      

          
            