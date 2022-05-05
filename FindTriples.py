import re
import networkx as nx
#import spacy


#nlp=spacy.load("en_core_web_sm")

f=open("C:/Users/22695/Desktop/gene-label.txt","r")
genes=f.read().split("\n")
genes=set(filter(lambda x: len(x)!=0,genes))
f.close()
f=open("C:/Users/22695/Desktop/protein-label.txt","r")
proteins=f.read().split("\n")
proteins=set(filter(lambda x: len(x)!=0,proteins))
f.close()
'''
f=open("C:/Users/22695/Desktop/NLP/Token.txt","r")
sentences=f.read().split("\n")
f.close()
print(len(sentences))

f=open("C:/Users/22695/Desktop/Sentence.txt","w")
for gene in genes:
    f.write(">gene|"+gene+"\n")
    for sentence in sentences:
        if " "+gene+" " in sentence:
            f.write(sentence+"\n")
for protein in proteins:
    f.write(">protein|"+protein+"\n")
    for sentence in sentences:
        if " "+protein+" " in sentence:
            f.write(sentence+"\n")
f.close()

gene=0
protein=0
f=open("C:/Users/22695/Desktop/Sentence.txt","r")
data=f.read().split("\n")
f.close()
for line in data:
    try:
        if(line[0]==">"):
            type=line.split("|")[0]
            if(type==">gene"):
                gene+=1
            elif(type==">protein"):
                protein+=1
            else:
                print("error!")
    except:
        print(line)
        next
print(gene,"gene occured!")
print(protein,"protein occured!")


f=open("C:/Users/22695/Desktop/NLP/test_out.tab","r")
text=f.read().split("\n")
f.close()
dic=dict()
for token in text[:-1]:
    label=token.split("\t")[2]
    name=token.split("\t")[0]
    if(label!="O"):
        if(label in dic):
            dic[label].append(name)
        else:
            dic[label]=[name]
for key in dic.keys():
    dic[key]=set(dic[key])
for key in dic.keys():
    print(key,":",len(dic[key]))

occur=set()
nonsense=["in","with","a","is","and","are","by","on","have"\
    ,"of","an","the","but","than","for","to","at"]
for key in dic.keys():
    temp=[]
    for value in dic[key]:
        if(value not in nonsense and value not in occur):
            occur.add(value)
            temp.append(value)
    dic[key]=temp
for key in dic.keys():
    print(key,":",len(dic[key]))

f=open("C:/Users/22695/Desktop/NLP/Token.txt","r")
sentences=f.read().split("\n")
f.close()

f=open("C:/Users/22695/Desktop/Entities.txt","w")
total=0
legal=0
for sentence in sentences:
    entities=[]
    total+=1
    for key in dic.keys():
        for value in dic[key]:
            if(" "+value+" " in sentence):
                entities.append((key,value))
    if(len(entities)):
        legal+=1
        f.write(">"+sentence+"\n")
        for entity in entities:
            f.write(entity[0]+"|"+entity[1]+"\n")
    if(total%10000==0):
        print(total,"sentences processed,",legal,"sentences saved.")
f.close()
print("Done!\n",total,"sentences processed,",legal,"sentences saved.")

f=open("C:/Users/22695/Desktop/Entities.txt","r")
data=f.read().split("\n")
f.close()

line=0

f=open("C:/Users/22695/Desktop/Triples.txt","w")
count=1
fail=0
while(line<len(data)):
    if(data[line][0]==">"):
        sentence=data[line][1:]
        entities=[]
        line+=1
        while(data[line][0]!=">"):
            entity=data[line].split("|")[-1]
            entities.append(entity)
            line+=1
        entities=set(entities)
        if(len(entities&genes)!=0 or len(entities&proteins)!=0):
            f.write(">"+sentence+"\n")
            doc=nlp(sentence)
            edges=[]
            try:
                for entity in entities:
                    if(entity in genes or entity in proteins):
                        for token in doc:
                            for child in token.children:
                                edges.append(('{0}'.format(token.lower_),'{0}'.format(child.lower_)))
                        graph=nx.Graph(edges)
                        for second_entity in entities:
                            if(second_entity==entity):
                                continue
                            distance=nx.shortest_path_length(graph,source=entity.lower(),\
                                                         target=second_entity.lower())
                            for token in doc:
                                if token.dep_ == 'ROOT':
                                    relation=(token.head.text)
                                    f.write('{0}\t{1}\t{2}\t{3}\n'.format(entity, relation, second_entity, distance))
                                    count+=1
            except:
                fail+=1
                next
            if(count%10000==0):
                print(count,"triples found,",fail,"failed.")
f.close()   
print(count,"triples found,",fail,"failed.") 
''' 
count=dict()
f=open("C:/Users/22695/Desktop/Triples.txt","r")
data=f.read().split("\n")
f.close()
f=open("C:/Users/22695/Desktop/Temp.txt","w")
cursent=""
for line in data:
    if(len(line) >1 and line[0]==">"):
        cursent=line
        continue
    triple=line.split("\t")
    if((triple[0] in genes or triple[0] in proteins) and (triple[2] in genes or triple[2] in proteins)):
        if(triple[0] in count):
            count[triple[0]].append(triple[1])
        else:
            count[triple[0]]=[triple[1]]
for key in count:
    ls=count[key]
    dic=dict()
    for i in ls:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    count[key]=dic
for key in count.keys():
    if("decreased" in count[key].keys()):
        print(key,count[key]["decreased"])
