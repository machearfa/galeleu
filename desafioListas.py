arenas = [
    [1200, 1500, 1100, 1800, 1700] #arena 1
    [1000, 950, 1100, 1500, 980]   #arena 2
    [2000, 1900, 1950, 2100, 2200] #arena 3
]








for medias in arenas:
    media1 = sum(medias[0]) / len()
    media2 = sum(medias[1]) / len()
    media3 = sum(medias[2]) / len()

    if media1 > media2 or media3:
        print('arena com o maior desempenho: arena1')
    elif media2 > media3 or 