# Get data from the morph.io api
import requests

# We're always asking for json because it's the easiest to deal with
morph_api_url = "https://api.morph.io/msinan52/msinan/data.json"

# Keep this key secret!
morph_api_key = "1zl4ZkNDSQ4u7lD7FHBQ"

r = requests.get(morph_api_url, params={
  'key': morph_api_key,
  'query': "select * from "data" limit 100000"
})

print r.json()
