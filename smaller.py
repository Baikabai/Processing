import os

def smaller(input_path,output_path):
    list_name = os.listdir(input_path)
    for name in list_name:
        lines = open(input_path+name,'r',encoding='utf-8').read()
        lines = lines.lower()
        output = open(output_path+name,'w',encoding='utf-8')
        output.write(lines)
        