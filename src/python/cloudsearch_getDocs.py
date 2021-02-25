import boto3
import json

# Get the service resource.
client = boto3.client('cloudsearchdomain', endpoint_url='http://search-botshiptracking-wnmcmnwxroxrdeksxm2htsgiqq.us-west-2.cloudsearch.amazonaws.com')

# Search Documents.
response = client.search(
    query="(and carrier_code: '02' (not tracking_status:'Returned to Sender') (not tracking_status:'shipped'))",
    queryParser='structured',
    returnFields='tracking_id,ship_date',
    size=10
)

#Print Data
print( json.dumps(response) )


