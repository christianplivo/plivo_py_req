import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')


# get the details of a Powerpack resource.
powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
print(powerpack)