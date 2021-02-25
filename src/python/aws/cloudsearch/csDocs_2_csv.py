import boto3
import json
import pandas as pd

# Get the service resource.
client = boto3.client('cloudsearchdomain', endpoint_url='http://search-botshiptracking-wnmcmnwxroxrdeksxm2htsgiqq.us-west-2.cloudsearch.amazonaws.com')

#Intialize
rows = []
contextMain = {"cursor": "initial", "found": 0, "retrieveCount": 0, "size": 10000, "moreRows": True}
rows.clear()

#Read CS and add to List
def loopCSDomain(context) :
    # Search Documents.
    response = client.search(
        query="(and tracking_status:'Delivered')",
        queryParser='structured',
        returnFields='tracking_id,ship_date',
        size=context['size'],
        cursor=context['cursor']
    )       

    #Append rows to list
    global rows
    rows = rows + response['hits']['hit']

    #update context
    contextMain['cursor'] = response['hits']['cursor']

    if len(response['hits']['hit']) < context['size']:
        contextMain['moreRows'] = False
    
while contextMain['moreRows'] == True:
    loopCSDomain(contextMain)

#Output to File
print("Total rows count - " + str(len(rows)))
data = pd.json_normalize(rows)

f = open("CS_2_csv.csv", "w")
f.write(data.to_csv())
f.close()
