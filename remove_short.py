import re
import os


def remove_short(path,pathout):
    name = os.listdir(path)
    for list_name in name:
        b = []
        f = open(path+list_name,'r',encoding='utf-8')
        data = f.readlines()
        for i in data:
            if len(i)>8:
                b.append(i)
        f.close()
        str = ''.join(b)
        str = re.sub('。','',str)
        file_out = open(pathout+list_name,'w',encoding='utf-8')
        file_out.write(str)

