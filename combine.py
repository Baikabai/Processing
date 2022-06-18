import os
def combine(input_path,outputfile):
    list_name = os.listdir(input_path)
    for name in list_name:
        f = open(input_path+name,'r',encoding='utf-8')
        lines = f.readlines()
        f.close()
        with open(outputfile,'a',encoding='utf-8') as g:
            for i,line in enumerate(lines):
                if i == 0:
                    continue
                elif i ==1:
                    continue
                else:
                    line = line.lstrip()
                    g.write(line)
            
        
