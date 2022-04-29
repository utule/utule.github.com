from turtle import color
import matplotlib.pyplot as plt

f=open("C:/Users/22695/Downloads/test_out.tab","r")
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
print(dic["B-Gene"])
print(dic["I-Gene"])
print(dic["B-Protein"])
print(dic["I-Protein"])

dic=sorted(dic.items(),key = lambda x:len(x[1]),reverse = True)
print(dic)
keys=[]
values=[]

count=dict()
for i in range(0,12):
    if(dic[i][0][2:] in count):
        count[dic[i][0][2:]]+=len(dic[i][1])
    else:
        count[dic[i][0][2:]]=len(dic[i][1])
plt.bar(list(count.keys()),list(count.values()),color="steelblue",edgecolor="black")
plt.title("Predicted number of partial labels")
plt.xlabel("Label")
plt.ylabel("Num")
plt.show()
