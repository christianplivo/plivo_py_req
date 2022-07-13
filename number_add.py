import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')

# API lets you add SMS- and MMS-enabled numbers to a number pool resource via Plivo’s SMS service.
powerpack = client.powerpacks.get(uuid="powerpack_uuid")
print(powerpack.add_number('your-number'))