import requests, json
from collections import Counter

def getEsData(index):
    param = {"query":{"filtered":{"query":{"range":{"@timestamp":{"gte":"now-10m", "lte": "now"}}}, "filter":{"term":{"signal_level": 6}}}}, "size": 1000}

    r = requests.get("http://10.1.0.82:9200/"+index+"/_search?pretty", json=param)
    #print r.json()["hits"]["total"]
    if (r.json()["hits"]["total"] > 0):
        return True
    else:
        return False

print getEsData("php-fpm")

