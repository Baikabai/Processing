import re
import os

def replace_numer(path,path_out):
    word = re.compile('^[a-zA-Z].*?[0-9]$')
    file_name_list = os.listdir(path)
    for name in file_name_list:
        b = []
    # Reading the file MecabNeologd_test.txt and splitting the words.
        with open(path+name,'r',encoding='utf-8') as f:
            data = f.read()
            words = data.split()
    
        for i in words:
            match = word.findall(i)
            if match:
                b.append(i)
            else:
                i = re.sub('\d+','0',i)
                b.append(i)
                b.append(' ')
        str = ''.join(b)
        with open(path_out+name,'w',encoding='utf-8')as g:
            g.write(str)