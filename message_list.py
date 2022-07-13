import plivo

client = plivo.RestClient('<auth_id>','<auth_token>')

# to filtering the records use message_state, message_direction, subaccount
response = client.messages.list(
    limit=5,  # The number of results per page
    offset=0,  # The number of value items by which the results should be offset
    # message_state="delivered",  # The state of the message to be filtered
    # message_direction="inbound",  # The direction of te message to be fltered
    # subaccount="SubAccount_AUTH_ID",  # The id of the subaccount, if SMS details of the subaccount is needed.
)
print(response)
