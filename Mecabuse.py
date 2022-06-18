import re
import MeCab
import sys
import neologdn
import mojimoji
import os


def Mecab(input_path,output_path):
    name = os.listdir(input_path)
    # A regular expression that matches all the characters in the string.
    code_regex = re.compile('[\t\s!"#$%&\'\\\\()*+,-./:;；：<=>?@[\\]^_`{|}~○｢｣「」〔〕“”〈〉'\
        '『』【】＆＊（）＄＃＠？！｀＋￥¥％♪…◇→←↓↑｡･ω･｡ﾟ´∀｀ΣДｘ⑥◎©︎♡★☆▽※ゞノ〆εσ＞＜┌┘]')

    for path_name in name:
        data = open(input_path+path_name, 'r',encoding="utf-8")
        textdata = data.read()
        textdata = re.sub('https?://[\da-zA-Z!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+', '', textdata)
        textdata = code_regex.sub('', textdata)
        textdata = neologdn.normalize(textdata)
        textdata = mojimoji.zen_to_han(textdata, kana=False)
        textdata = textdata.lower()
        textdata = textdata.strip()
        mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        mecab.parse('')
        results = []
        lines = textdata.split("\r\n")
        for line in lines:
            r = []
            s = line
            s = s.replace("|", "")
            s = re.sub(r'《.+?》', "", s)
            s = re.sub(r'［.+?］', '', s)
            # Mecab
            node = mecab.parseToNode(s)
            while node:
                if node.feature.split(",")[6] == '*':
                    word = node.surface
                else:
                    word = node.feature.split(",")[6]
                part = node.feature.split(",")[0]

# A part of speech tagger.
                if part in ["名詞", "形容詞", "動詞"]:
                    r.append(word)
                elif word =="。":
                    r.append(word)
                node = node.next
            rl = (" ".join(r)).strip()
            results.append(rl)
        with open(output_path+path_name,'w',encoding='utf-8') as f: 
            f.write("\n".join(results))