from c8 import C8Client
import os

key = os.environ['MACROMETA_APIKEY']

collection_name = "sessionId"
host = "api-vimba-473191d1-eu-central.paas.macrometa.io"
geoFabric = "Europe"

# Create a connection to GDN
client = C8Client(protocol='https', host=host, geofabric=geoFabric, port=443, apikey=key)

# Create a new collection if it does not exist
if client.has_collection(collection_name):
    print("Collection exists")
else:
    client.create_collection_kv(name=collection_name)