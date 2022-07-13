import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')


# deletes a single powerpack. cannot be undone
powerpack = client.powerpacks.get(uuid="powerpack_uuid")
print(powerpack.delete(False))