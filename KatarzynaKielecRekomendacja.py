###  W    zorowane na przykładzie Rona Zacharskiego
##
##from math import sqrt
##
##users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
##         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
##         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
##         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
##         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
##         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
##         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
##         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
##        }
##
##
##
##def manhattan(rating1, rating2):
##    #Oblicz odległość w metryce taksówkowej miedzy dwoma  zbiorami ocen
##    # danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
##    #Zwróć -1, gdy zbiory nie mają wspólnych elementów
##
##    Osoba1=rating1.keys()
##    Osoba2=rating2.keys()
##    distance=0
##    # dystans od wszystkich 
##    distanceAll=0
##    
##
##    for osob in Osoba1:  #
##        if osob in rating2.keys():
##            distanceAll=distanceAll+abs(rating2[osob]-rating1[osob])
##            return distanceAll
##        else:
##            return -1
##
##
##def computeNearestNeighbor(username, users):
##    #zwracanie listy najblizszych sasiadow
##
##    nameOfNearestNeighbor=""
##    distances = []
##    user =""
##
##    for user in users:
##        if user!=username:
##            distance=0
##            distance=manhattan(users[username],users[user])
##            distances.append((distance, user))
##    return sorted(distances)
##
##    NajblizszySasiad=sorted(distances)
##    print(NajblizszySasiad[0])
##    return NajblizszySasiad[0] # zero zwraca pierwsze użytkowanika z listy
##
##recommendations=[]
##
##def recommend(username, users):
##    #Zwróć listę rekomendacji dla użytkownika
##    # znajdź preferencje najbliższego sąsiada
##
##    nearest = computeNearestNeighbor(username, users)[0][1]
##    print('Najblizszy sasiad to: %s' % nearest)
##
##    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
##
##    ratingOfNearest=users[nearest]
##    print('Rekomendaje uzytkownika: ')
##    print(ratingOfNearest)
##
##    userRating=users[username]
##
##    for artists in ratingOfNearest:
##        if not artists in userRating:
##            recommendations.append((artists,ratingOfNearest[artists]))
##    #zwracanie posortowanych rekomendacji dla uzytkownika (artyste ocenil jego sasiad)
##    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
##
##
##print(recommend('Fruzia', users))
##
