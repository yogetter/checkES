import requests, json
from collections import Counter

def getEsData(index):
    param = {"query":{"range":{"timestamp":{"gte":"now-1h", "lte": "now"}}}, "size": 10000}
    r = requests.get("http://10.1.0.82:9200/"+index+"/_search?pretty", json=param)
    i = 1
    userCount={}
    for item in  r.json()["hits"]["hits"]:
        print "No.", i, item['_source']['user'].decode('unicode_escape')
        print
        i += 1
        index = item['_source']['user'].decode('unicode_escape')
        if( userCount.has_key(index)):
            userCount[index] += 1
        else:
            userCount[index] = 1
            
    print json.dumps(userCount, encoding="utf-8", ensure_ascii=False) 
    print "Total login: ", r.json()["hits"]["total"]

getEsData("owncloud-login")

