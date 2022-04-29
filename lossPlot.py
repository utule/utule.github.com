import matplotlib.pyplot as plt
import re

f = open("C:/Users/22695/Desktop/LSTMresult.txt")
data = f.readlines()
f.close()
y=[]
data.pop()
for line in data:
    line=str(line)
    if(line[0:4]=="loss"):
        y.append(line.split(" ")[-1])
for i in range(0,len(y)):
    y[i]=str(y[i]).strip("\n")
    y[i]=float(y[i])
x=[x for x in range(1,101)]
print(len(y))
plt.plot(x,y)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("loss of epoch")
f = open("C:/Users/22695/Desktop/log.4-11.txt")
data = f.readlines()
f.close()
x=list(range(1,101))
for i in range(0,99):
    y[i]=1000
for line in data:
    line=str(line).strip("\n")
    if(re.search("Epoch: ",line)):
        idx=line[49:].split(",")[0]
        loss=line[49:].split(" ")[-1]
        idx=int(idx)
        loss=float(loss)
        y[idx-1]=min(y[idx-1],loss)
print(len(y))
plt.plot(x,y)
plt.legend(["LSTM-CRF","BERT-CRF"],loc="upper right")
plt.savefig("C:/Users/22695/Desktop/figure1.png")
plt.show()

