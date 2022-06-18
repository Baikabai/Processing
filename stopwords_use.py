import re
import os
def remove_stopwords(words,stopwords):
    """
    It takes a list of words and a list of stopwords as input, and returns a list of words that are not
    stopwords
    
    :param words: a list of words
    :param stopwords: a list of words that we want to remove from our text
    :return: A list of words that are not in the stopwords list.
    """
    words = [w for w in words if w not in stopwords]
    return words
def remove_frequencywords(words1,frequencywords):
    """
    It takes a list of words and a list of frequency words and returns a list of words that are not in
    the frequency words list
    
    :param words1: list of words
    :param frequencywords: a list of words that are to be removed from the text
    :return: A list of words that are not in the frequencywords list.
    """

    words1 = [w for w in words1 if w not in frequencywords]
    return words1
def stopwordsopen(stopwords_path):
    """
    It takes a path to a file that contains a list of stopwords and returns a list of stopwords
    
    :param stopwords_path: path to a file that contains a list of stopwords
    :return: a list of stopwords
    """
    stopwords = open(stopwords_path, 'r', encoding='utf-8')
    stopwords = stopwords.read().splitlines()
    return stopwords
    # Reading the file and stripping the words.
def frequencywordsopen(frequencywords_path):
    """
    It takes a path to a file that contains a list of frequency words and returns a list of frequency words
    
    :param frequencywords_path: path to a file that contains a list of frequency words
    :return: a list of frequency words
    """
    frequencywords = open(frequencywords_path, 'r', encoding='utf-8')
    frequencywords = frequencywords.read().splitlines()
    return frequencywords

def stopwords_use(path,path_out,stopwords_file,frequencywords_file):    
    path = 'E:/M2/nohave/mecab/'
    path_out = 'E:/M2/nohave/mecab1/'
    file_name_list = os.listdir(path)
    for name in file_name_list:
    # Reading the file MecabNeologd_test.txt and splitting the words.
        with open(path+name,'r',encoding='utf-8') as f:
            data = f.read()
            words = data.split()

        #Then it is removing the stopwords
        # from the words and joining the words.
        stopwords = stopwordsopen(stopwords_file)
        frequencywords = frequencywordsopen(frequencywords_file)
        stop_text = remove_stopwords(words,stopwords)
        stop_text = remove_frequencywords(stop_text,frequencywords)
        stop_string = ' '.join(stop_text)
        # Converting all the words to lower case.

        # stop_string = re.sub(u"\\d+", "0", stop_string)

        # Writing the stop_string to the file stop-words_test.txt.
        with open(path_out+name,'w',encoding='utf-8') as outputfile:
            outputfile.write(stop_string)