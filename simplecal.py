import cv2
import numpy
import os

f = open('C:\\Users\\DAREWIN\\Desktop\\data.txt', 'w')

n = 80
while n < 90:
    path = 'C:\\Users\\DAREWIN\\Base de donne\\DB LSF Mots\\new2502\\2020-02\\avoir\\' + str(n+1)
    moyenne = 0
    sum_img = []
    for dir in os.listdir(path):  # 获取当前目录下所有文件夹和文件(不带后缀)的名称
        filePath = os.path.join(path, dir)  # 得到文件夹和文件的完整路径
        # (filepath, tempfilename) = os.path.split(filePath)
        # (filename, extension) = os.path.splitext(tempfilename)
        # print(filename)
        img = cv2.imread(filePath)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir en valeur en niveaux de gris
        sum_img.append(img_gray)  # Rassemblez toutes les images
        # moyenne = sum(moyenne_list)/len(moyenne_list)  # Moyenne de toutes les images du fichier
        # sum_ndg = sum(sum(sum(sum_img)))
    moyenne = numpy.average(sum_img)
    # ecart_type = numpy.std(sum_img)
    # mediane = numpy.median(sum_img)
    print(moyenne)
    f.write(str(moyenne))
    f.write('\n')
    n += 1
