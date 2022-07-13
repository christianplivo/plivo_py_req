import plivo
import json

client = plivo.RestClient('<auth_id>','<auth_token>')


# API lets you to create a Powerpack via Plivo’s SMS service.
number_priorities = [{'country_iso': 'US',
                     'priority': {'priority1': 'shortcode',
                     'priority2': 'longcode', 'priority3': 'tollfree'},
                     'service_type': 'SMS'}]
powerpack = client.powerpacks.create(name="<new_powerpack_name>",sticky_sender=True, number_priority=number_priorities)
print(powerpack)