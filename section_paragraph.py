import os


def section_paragraph(path,pathout):
    print("completed all of the files")
    path = 'E:/M2/nohave/mecab/'
    pathout = 'E:/M2/nohave/mecab1/'
    name = os.listdir(path)
    for list_name in name:
        b = []
        f = open(path+list_name,'r',encoding='utf-8')
        data = f.read()
        for i in data:
            b.append(i)
            if i == '。':
                b.append('\n')
        str = ''.join(b)
        g = open(pathout+list_name,'w',encoding='utf-8')
        g.write(str)
        g.close()