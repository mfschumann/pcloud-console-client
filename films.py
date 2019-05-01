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
        liste_films.sort()
    choix = input('Voulez-vous continuer (o/n) ?')
    print('')
print(liste_films)