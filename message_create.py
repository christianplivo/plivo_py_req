import plivo

# The SDK uses consistent interfaces to create, retrieve, update, delete and list resources.
# .create(*args, **kwargs)
# .get(id=resource_identifier)
# .update(id=resource_identifier, *args, **kwargs) 
# .delete(id=resource_identifier)
# .list()

client = plivo.RestClient("<auth_id>", "<auth_token>")

# create a message 
response = message_created = client.messages.create(
    src='+19183836434',
    dst='+15107171878',
    text='Hello, world!'
)


# create a bulk message by using the same call with "<" as a delimiter 
# response = message_created = client.messages.create(
#     src='+19183836434',
#     dst='+15107171877<+15104150191',
#     text='Hello, world!'
# )

print('message sent.')

# print message response
print(response)

# print message uuid
#print(response.message_uuid)
