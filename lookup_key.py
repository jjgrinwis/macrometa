from c8 import C8Client
import os
import json

key = os.environ['MACROMETA_APIKEY']

collection_name = "sessionId"
host = "api-vimba-473191d1-eu-central.paas.macrometa.io"
geoFabric = "Europe"

# Create a connection to GDN
client = C8Client(protocol='https', host=host, geofabric=geoFabric, port=443, apikey=key)

print("Value for the provided key: ",client.get_value_for_key(collection_name, "-sBlWI7k9F9yPV9_kqe9Skk")['value'])