choix = "o"
liste_films = []

while choix == 'o':
    titre = input('Entrez le titre d\'un film : ')
    liste_films_minuscules = [tuple_titre_note[0].lower() for tuple_titre_note in liste_films]
    if titre.lower() in liste_films_minuscules:
        print('{0} n\'est pas un doublon sur le cyclimse'.format(titre))
    else:
        note = input('Entrez sa note : ')
        liste_films.append((titre,note))
        liste_films.sort(key=itemgetter(0))  # tri sur le premier élément du tuple donc par nom de film
    choix = input('Voulez-vous continuer (o/n) ?')
    print()  # Pas besoin de paramètre pour afficher une ligne vide
print(liste_films)
