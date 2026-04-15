MAX_WIDTH = 100

# Dictionnaire contenant toutes les phrases
# Certaines sont dans le dictionnaire mais ne s'affichent pas (cf. blocs_affichage)
phrases = {
    'bloc1_phrase1': 'le code propre facilite la maintenance',
    'bloc2_phrase1': 'tester souvent évite beaucoup d\'erreurs',
    'bloc2_phrase2': 'cette phrase ne doit pas s\'afficher',
    'bloc3_phrase1': 'cette phrase ne doit pas s\'afficher',
    'bloc3_phrase2': 'un bon code doit rester simple et clair',
    'bloc3_phrase3': 'la simplicité améliore la qualité du code',
    'bloc3_phrase4': 'refactoriser améliore la compréhension',
}

# Structure d'affichage : définit l'ordre et les phrases affichées
# Modifiez cette liste pour changer l'ordre ou exclure des phrases
blocs_affichage = [
    ['bloc1_phrase1'],
    ['bloc2_phrase1'],
    ['bloc3_phrase3', 'bloc3_phrase4'],
]


def afficher_bloc(textes, largeur_max=MAX_WIDTH):
    if not textes:
        return
    
    textes_minuscules = [texte.lower() for texte in textes]
    largeur_contenu = largeur_max - 4
    ligne_bordure = '+' + '-' * (largeur_max - 2) + '+'
    
    print(ligne_bordure)
    
    for texte in textes_minuscules:
        if len(texte) <= largeur_contenu:
            ligne = f"| {texte.ljust(largeur_contenu)} |"
            print(ligne)
        else:
            mots = texte.split()
            ligne_actuelle = ""
            
            for mot in mots:
                if len(ligne_actuelle) + len(mot) + 1 <= largeur_contenu:
                    if ligne_actuelle:
                        ligne_actuelle += " " + mot
                    else:
                        ligne_actuelle = mot
                else:
                    if ligne_actuelle:
                        print(f"| {ligne_actuelle.ljust(largeur_contenu)} |")
                    ligne_actuelle = mot
            
            if ligne_actuelle:
                print(f"| {ligne_actuelle.ljust(largeur_contenu)} |")
    
    # Afficher la bordure inférieure
    print(ligne_bordure)
    print()


def afficher_tous_blocs(phrases_dict, structure_blocs, largeur_max=MAX_WIDTH):
    for bloc in structure_blocs:
        textes = [phrases_dict[cle] for cle in bloc if cle in phrases_dict]
        afficher_bloc(textes, largeur_max)


if __name__ == '__main__':
    print("=" * MAX_WIDTH)
    print("AFFICHAGE DES BLOCS DE TEXTE ENCADRÉS".center(MAX_WIDTH))
    print("=" * MAX_WIDTH)
    print()
    afficher_tous_blocs(phrases, blocs_affichage, MAX_WIDTH)
