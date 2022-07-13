import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')


# API can be used to fetch a list of numbers from the Number Pool based on number_pool_UUID specified in the resource URI.
powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
print(powerpack.list_numbers(starts_with=512, country_iso2='US'))