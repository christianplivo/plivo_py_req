import plivo


client = plivo.RestClient("<auth_id>", "<auth_token>")


# API call returns the details of the media files identified by the media_uuid specified in the request URL.
response = client.media.get('media_id')

# List media can use arguments "limit" and "offset"
# response = client.media.list()
print(response)