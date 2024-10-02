#pgzero
# Hücrelerden oluşan oyun penceresi
hucre_g = 7 # Hücrenin genişliği
hucre_h = 7 # Hücrenin yüksekliği
WIDTH = 50 * hucre_g
HEIGHT = 50 * hucre_h
hucre = Actor('sınır')
hucre.width = 50
hucre.height = 50
TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

haritam = [[0, 0, 0, 0, 0, 0, 0],
           [0, 1, 2 , 1, 3, 1, 0],
           [0, 1, 1, 2, 1, 1, 0],
           [0, 3, 2, 1, 1, 3, 0],
           [0, 1, 1, 1, 3, 1, 0],
           [0, 1, 3, 1, 1, 2, 0],
           [0, 0, 0, 0, 0, 0, 0]]

def harita_ciz():
    for i in  range(len(haritam)): 
        for j in  range(len(haritam[0])): 
            if haritam[i][j] == 0:
                hucre.image = 'sınır'
                hucre. left = hucre.width * j
                hucre. top = hucre.height * i
                hucre. draw ( )

            elif haritam[i][j] == 1:
                hucre.image = 'zemin'
                hucre. left = hucre.width * j
                hucre. top = hucre.height * i
                hucre. draw ( )
                
            elif haritam[i][j] == 2:
                hucre.image = 'çatlak'
                hucre. left = hucre.width * j
                hucre. top = hucre.height * i
                hucre. draw ( )

            elif haritam[i][j] == 3:
                hucre.image = 'kemikler'
                hucre. left = hucre.width * j
                hucre. top = hucre.height * i
                hucre. draw ( )
        
def draw():
    hucre.draw()
    harita_ciz()
    
