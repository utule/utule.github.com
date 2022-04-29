import re
import requests
import time

term=["AD"]
save_file="C:/Users/22695/Desktop/NLP/pubmed_data/"
page=[10000,10400]

url1="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term="
url2="http://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids="

s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5


pubmed_id=[]
start_page=page[0]
while(start_page<=page[1]):
    url=url1
    for i in term:
        url += i
        url += " AND "
    url=url[:-5]
    url+="&retstart="+str(start_page)                                                                                                                                    
    r=requests.get(url=url)
    r.encoding="utf-8"
    text=r.text.split("\n")
    for i in text:
        if(re.match("<Id>",i)):
            pubmed_id.append(i[4:-5])
    start_page+=20
print(len(pubmed_id))

#unique 
#pubmed_id = list(set(pubmed_id))  
#print(len(pubmed_id))

for id in pubmed_id:
    url=url2+id
    r=requests.get(url)
    r.encoding="utf-8"
    text=r.text
    #if (len(text)==0):
    #    continue
    file=save_file+id+".txt"
    f=open(file,"w")
    f.write(text)
    f.close
    time.sleep(5)

