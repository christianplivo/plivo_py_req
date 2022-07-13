import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')

# retrieves the details of the specified number from the number pool resource.
powerpack = client.powerpacks.get(uuid="powerpack_uuid")
print(powerpack.find_number('your-number'))