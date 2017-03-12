import os
import string

def rename_files():

    # get all the files
    
    file_list = os.listdir(r"E:\prog fundamentals with python\prank\prank")
    print(file_list)
    print("hello")
    os.chdir(r"E:\prog fundamentals with python\prank\prank")
    # rename files
    for file_name in file_list:
        map = str.maketrans('', '', '0123456789')
        os.rename(file_name,file_name.translate(map))    
        
rename_files()
