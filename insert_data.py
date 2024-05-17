from c8 import C8Client
import os
import json

key = os.environ['MACROMETA_APIKEY']

collection_name = "sessionId"
host = "api-vimba-473191d1-eu-central.paas.macrometa.io"
geoFabric = "Europe"

# Create a connection to GDN
client = C8Client(protocol='https', host=host, geofabric=geoFabric, port=443, apikey=key)

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# our KV data we're going to insert:
data = [
    {
      "value": json.dumps(x),
      "expireAt": 0
    }
  ]

client.insert_key_value_pair(collection_name, data)
print("KV Pairs Inserted")