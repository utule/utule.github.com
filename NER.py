import os
import spacy
import re

nlp=spacy.load("en_core_web_sm")

file="C:/Users/22695/Desktop/NLP/pubmed_data"
outputFile="C:/Users/22695/Desktop/output.txt"
total_num=0
for filepath,dirnames,filenames in os.walk(file):
    for filename in filenames:
        f=open(os.path.join(filepath,filename),"r")
        text=f.read().split("\n")[1][11:]
        f.close()
        text_sentences=nlp(text)
        for sentence in text_sentences.sents:
            doc=nlp(sentence.text)
            str=""
            for token in doc:
                if(re.search("\s",token.text)):
                    continue
                str+=token.text+"/O "
            str=str.strip(" ")
            str+="\n"
            f=open(outputFile,"a")
            f.write(str)
            f.close()
        total_num+=1
print(total_num," processed in total.")