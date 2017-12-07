import requests
from collections import Counter

def getEsData(index):
    r = requests.get("http://10.1.0.82:9200/"+index+"/_search?pretty")
    length = r.json()["hits"]["total"]
    param = { "size" : length}
    print length
    r = requests.get("http://10.1.0.82:9200/"+index+"/_search?pretty", json=param)
    print len(r.json()["hits"]["hits"])
    all_user = ""
    for item in  r.json()["hits"]["hits"]:
        try:
            all_user += item["_source"]["user"] + "\n"
        except KeyError:
            continue
    return all_user

data += getEsData("owncloud-login")

result = Counter(data.split())
for i in result.most_common(15):
    print i

