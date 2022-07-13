import plivo

client = plivo.RestClient('<auth_id>','<auth_token>')


# retrieves a Message Detail Record (MDR).
response = client.messages.get(message_uuid="your_message_uuid").listMedia()
print(response)