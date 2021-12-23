# -*- coding:utf-8 -*-
import os.path
# Définissez une fonction, path est votre chemin
def traversalDir_FirstDir(path):
    # Définissez une liste pour stocker les résultats
    list = []
    # Déterminer si le chemin existe
    if (os.path.exists(path)):
        # Récupère tous les fichiers ou dossiers du répertoire
        files = os.listdir(path)
        for file in files:
            # Obtenez le chemin de tous les répertoires sous le fichier
            m = os.path.join(path, file)
            # Déterminer si un dossier se trouve dans ce chemin
            if (os.path.isdir(m)):
                h = os.path.split(m)
                # print(h[1])
                list.append(eval(h[1]))
        list.sort()
        # print(list)
        return list




# traversalDir_FirstDir("E:\\xlrd-1.0.0")

# image_path = 'C:\\Users\\DAREWIN\\Base de donne\\DB LSF Mots\\01_bonjour\\1'
# # 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# # 输入文件夹路径、空文件列表[]
# # 返回 文件列表Filelist,包含文件名（完整路径）
# def get_filelist(dir, Filelist):
#     newDir = dir
#     if os.path.isfile(dir):
#         Filelist.append(dir)
#         # # 若只是要返回文件文，使用这个
#         # Filelist.append(os.path.basename(dir))
#     elif os.path.isdir(dir):
#         for s in os.listdir(dir):
# # 如果需要忽略某些文件夹，使用以下代码
# # if s == "xxx":
# # continue
#             newDir = os.path.join(dir, s)
#             get_filelist(newDir, Filelist)
#             return Filelist
#
# if __name__ == '__main__':
#     list = get_filelist('C:\\Users\\DAREWIN\\Base de donne\\DB LSF Mots\\01_bonjour', [])
#     print(len(list))
#     for e in list:
#         print(e)