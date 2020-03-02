import cv2 as cv


cv.namedWindow("TestImg")


i = 10
while i < 63:

    img = cv.imread("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/0000000"+str(i)+".jpg")

    print("C:/Users/DAREWIN/Base de donne/DB LSF Mots/01_bonjour/1/0000000"+str(i)+".jpg")

    cv.imshow("TestImg", img)

    i = i + 1
    k = cv.waitKey(200)

cv.waitKey(0)
cv.destroyAllWindows()

