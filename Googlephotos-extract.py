import os
import zipfile

rar = "C:\\Users\\raajv\\Downloads\\pictures"
os.chdir(rar)
for all in os.listdir(rar):
    if all[:7 ] =="takeout" and all[-3: ] =="zip":
        fname = os.path.abspath(all)
        awe = zipfile.ZipFile(fname)
        awe.extractall(rar)
        awe.close()

"""
pictures is for directory where pictures should be copied

videos is for directory where videos should be copied

"""
p = rar + "\\Takeout\\Google Photos"
pictures = "C:\\Users\\raajv\\Downloads\\pictures\\Takeout\\pictures"

videos = "C:\\Users\\raajv\\Downloads\\pictures\\Takeout\\videos"

os.chdir(p)
ld = os.listdir(os.getcwd())
for i in ld:
    os.chdir(p + "\\" + i)
    ld1 = os.listdir(os.getcwd())
    for j in ld1:

        if j[-3:] == "jpg" or j[-3:] == "png" or j[-3:] == "jpeg" or j[-3:] == "gif":
            check = os.listdir(pictures)
            if j not in check:
                os.system("copy \"" + os.getcwd() + "\\" + j + "\" \"" + pictures + "\"")
            else:
                pass

        if j[-3:] == "mp4" or j[-3:] == "avi" or j[-3:] == "mov" or j[-3:] == "wmv":
            check = os.listdir(videos)
            if j not in check:
                os.system("copy \"" + os.getcwd() + "\\" + j + "\" \"" + videos + "\"")
            else:
                pass

