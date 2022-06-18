import os
def remove_space(input_path,output_path):
    name = os.listdir(input_path)
    for list_name in name:
        f = open(input_path+list_name,'r',encoding='utf-8')
        data = f.readlines()
        data_out = []
        for i in data:
            data = i.lstrip()
            data_out.append(data)
        data_out1 = ''.join(data_out)
        file_out = open(output_path+list_name,'w',encoding='utf-8')
        file_out.write(data_out1)