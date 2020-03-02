import numpy as np
import cv2

# Obtenez la première image du cadre
frame1 = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/000000000.jpg")
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)   # Convertissez le frame en niveaux de gris

magMin = 0
magMax = 0

n = 1
j = 0
magVideo = np.zeros((frame1.shape[0], frame1.shape[1], 64))  # Initialisation du tableau pour stocker le mag
tabNumpx = np.zeros(64)

# une boucle pour calculer la valeur de mag
while j < 64:

    if j < 10:
        frame2 = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/00000000" + str(j) + ".jpg")
    else:
        frame2 = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/0000000" + str(j) + ".jpg")
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Renvoie un vecteur de flux optique à deux canaux, qui est en fait la valeur de déplacement de pixel de chaque point,
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # print(flow.shape)
    # print(flow[..., 0])
    # Convertissez les coordonnées cartésiennes en coordonnées polaires pour obtenir l'axe polaire et l'angle polaire
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    magVideo[..., j] = mag
    # trouver la valeur du max et du min pour une fonction de normalization
    if magMax < np.amax(mag):
        magMax = np.amax(mag)
    if magMin > np.amin(mag):
        magMin = np.amin(mag)
    prvs = next
    j += 1

print('fin min max')
# une boucle pour calculer le nombre du pixel
i = 0
while i < 64:

    force = ((magVideo[..., i] - magMin)*255) / (magMax - magMin)  # normalize
    force = force.astype(np.uint8)

    # force = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    h, w = force.shape
    # print(flow.shape)

    segm = np.zeros([h, w])
    numpx = 0
    for row in range(h):
        for col in range(w):
            px = force[row, col]
            if px > 30:
                segm[row, col] = 255   # visualisation
                numpx += 1
    tabNumpx[i] = numpx

    print("numero "+str(n)+"  ||  "+"%09d.jpg" % i)
    cv2.imshow('frame2', segm)  # afficher les image de movement.
    n += 1

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    i += 1

print(tabNumpx)
listNumpx = tabNumpx.tolist()
print(listNumpx)
numImg = np.zeros(30, dtype=int)
# une boucle pour choisir 30 images qui sont plus important
m = 0
while m < 30:

    maxPx = np.amax(tabNumpx[...])
    numImg[m] = int(listNumpx.index(maxPx))
    tabNumpx[numImg[m]] = -1
    m += 1
print(numImg)
length = len(numImg)
# mise en ordre
for a in range(length):
    for b in range(0, length-a-1):
        if numImg[b+1] < numImg[b]:
            numImg[b], numImg[b+1] = numImg[b+1], numImg[b]
print(numImg)

image = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/000000000.jpg")
cv2.imwrite("C:/Users/DAREWIN/Base de donne/30 image cle/01_bonjour/1/" + "debut" + ".jpg", image)
# une boucle pour stocker les 30 images dans l'ordre
c = 0
for c in range(length):

    print(numImg[c])
    if numImg[c] < 10:
        image = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/00000000" + str(int(numImg[c])) + ".jpg")
    else:
        image = cv2.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/0000000" + str(int(numImg[c])) + ".jpg")
    cv2.imwrite("C:/Users/DAREWIN/Base de donne/30 image cle/01_bonjour/1/%08d.jpg" % c, image)

cv2.destroyAllWindows()
