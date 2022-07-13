import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')


# removes the number from the number pool resource.
powerpack = client.powerpacks.get(uuid="powerpack_uuid")
print(powerpack.remove_number('your-number'))