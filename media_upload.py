import plivo

client = plivo.RestClient("<auth_id>", "<auth_token>")

# API lets you upload media files to be used in sending MMS messages. Plivo supports up to 10 attachments in an upload API/SDK call with a maximum of 2MB per attachment. 
response = client.media.upload(['<video/image file path>', '<video/image file path>'])
print(response)