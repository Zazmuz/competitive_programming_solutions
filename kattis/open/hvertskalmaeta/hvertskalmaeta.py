distance_from_rejkiavik = {"Reykjavik": 0,
                           "Kopavogur": 6,
                           "Hafnarfjordur": 12,
                           "Reykjanesbaer": 48,
                           "Akureyri": 388,
                           "Gardabaer": 9,
                           "Mosfellsbaer": 16,
                           "Arborg": 64,
                           "Akranes": 49,
                           "Fjardabyggd": 659,
                           "Mulathing": 603,
                           "Seltjarnarnes": 4}

distance_from_akureyri = {"Reykjavik": 388,
                          "Kopavogur": 387,
                          "Hafnarfjordur": 391,
                          "Reykjanesbaer": 427,
                          "Akureyri": 0,
                          "Gardabaer": 389,
                          "Mosfellsbaer": 371,
                          "Arborg": 428,
                          "Akranes": 350,
                          "Fjardabyggd": 290,
                          "Mulathing": 216,
                          "Seltjarnarnes": 390}
name = input()
print("Reykjavik" if distance_from_rejkiavik[name] < distance_from_akureyri[name] else "Akureyri")