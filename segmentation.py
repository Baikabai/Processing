#coding:utf-8
import os


def cutFile(FileName,number):
    
    print("loading...")
    Data = open(FileName,'r',encoding='utf-8')
    
    List_num = Data.read().splitlines()
    n = len(List_num)
    p = n//number + 1
    
    print("starting···")
    
    
# A loop.
    for i in range(number):
        print("Generating "+str(i+1)+"subfile")
        destFileName = os.path.splitext(FileName)[0]+str(i+1)+".txt" 
        destFileData = open(destFileName,"w",encoding='utf-8')
        if(i==number-1):
            for line in List_num[i*p:]:
                destFileData.write(line+'\n')
        else:
            for line in List_num[i*p:(i+1)*p]:
                destFileData.write(line+'\n')
        destFileData.close()
        
    print("completed all of the files")