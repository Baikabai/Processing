from Processing.stopwords_use import frequencywordsopen
import segmentation as seg
import Mecabuse
import stopwords_use
import replace_number
import section_paragraph
import remove_space
import remove_short
import smaller
import combine


if __name__ == '__main__': 
    # if you want to use this code, you need to install MeCab and neologdn.
    # if you don't need to segmentation, you can delete the following three lines.
    # Filename = 'filename you need to segment'
    # number = 'number of subfiles you want to generate'
    # seg.segmentation(Filename,number)
    input_path = './input/'
    output_path = './output/'
    stopword = './stopword.txt'
    frequencyword = './frequencyword.txt'
    outputfile = './outputfile.txt'
    Mecabuse.Mecab(input_path,output_path)
    stopwords_use.stopwords_use(output_path,input_path,stopword,frequencyword)
    replace_number.replace_numer(input_path,output_path)
    section_paragraph.section_paragraph(output_path,input_path)
    remove_space.remove_space(input_path,output_path)
    remove_short.remove_short(output_path,input_path)
    smaller.smaller(input_path,output_path)
    combine.combine(input_path,outputfile)
    