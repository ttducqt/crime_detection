# this program delete the space in the name of file:
# example: armas (1).jpg -> armas(1).jpg

import os

def rename_file():
    list_folder = ["images", "labels"]
    for folder in list_folder:
        for filename in os.listdir(folder):
            dst = folder+"/"+filename.replace(" ", "")
            os.rename(folder+"/"+filename, dst)       
        
rename_file()


