import plivo

client = plivo.RestClient('<auth_id>','<auth_token>')

response = client.messages.get(
        message_uuid='c22f9e00-02fb-11ed-8306-0242ac110004',# Message UUID for which the details have to be retrieved
)
 # Prints the number of SMS units
print ("Your SMS was split into %s units" % response['units'])

# Sample successful output
# Your SMS was split into 4 units

# Prints the status of the message
print (response['message_state'])

# Sample successful output
# delivered

# Prints all the details of a message
print(response)
