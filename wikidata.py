import mkwikidata
import pandas as pd
import requests
import json


url = "https://hf.space/embed/hnam/start/hello"
yyy='you'
r = requests.post(
    url,
    data=json.dumps({"input": "German:i miss {}".format(yyy)}),
    headers={"Content-Type": "application/json"},
)

print( r.json())



# query = """
# SELECT DISTINCT ?cityLabel ?population ?gps
# WHERE
# {
#   ?city wdt:P31/wdt:P279* wd:Q515 .
#   ?city wdt:P1082 ?population .
#   ?city wdt:$id2 ?gps .
#   SERVICE wikibase:label {
#     bd:serviceParam wikibase:language "en" .
#   }
# }
# ORDER BY DESC(?population) LIMIT $id OFFSET $offset
# """
# query_result = mkwikidata.run_query(query, params={"offset": 10 ,"id": 10 ,"id2": "P625" })
# #print(query_result)

# data = [{"name" : x["cityLabel"]["value"], "population" : int(x["population"]["value"])} for x in query_result["results"]["bindings"]]


# city = pd.DataFrame(data).set_index("name")

# print(city.head(20))

