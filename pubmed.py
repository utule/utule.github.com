import re
import requests
import time

term=["AD"]
save_file="C:/Users/22695/Desktop/pubmed/"
page=[400,4000]

url1="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term="
url2="http://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids="

start=int(page[0]/20)
end=int(page[1]/20)
pubmed_id=[]
for page in range(start,end):
    url=url1
    for i in term:
        url += i
        url += " AND "
    url=url[:-5]
    url+="&retstart="+str(page)
    r=requests.get(url=url)
    r.encoding="utf-8"
    text=r.text.split("\n")
    for i in text:
        if(re.match("<Id>",i)):
            pubmed_id.append(i[4:-5])
print(len(pubmed_id))
for id in pubmed_id:
    url=url2+id
    r=requests.get(url)
    r.encoding="utf-8"
    text=r.text
    if (len(text)==0):
        continue
    file=save_file+id+".txt"
    f=open(file,"w")
    f.write(text)
    f.close
    time.sleep(5)


