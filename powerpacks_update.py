import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')

# define variables
params = {}
number_priorities = [
    {'country_iso': 'US',
    'priority': {'priority1': 'longcode', 'priority2': 'tollfree', 'priority3': 'shortcode'},
    'service_type': 'SMS'
    }]
params["name"] = "<update_powerpack_name>"
params["number_priority"] = number_priorities

# get the details of a Powerpack resource.
powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")

# Change a Powerpack’s name, sticky_sender, local_connect, or the application connected to it.
response = powerpack.update(params)
print(response)