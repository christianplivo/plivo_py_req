from typing import Text
import plivo

client = plivo.RestClient("<auth_id>", "<auth_token>")

# SMS containing more than 160 standard characters, is automatically split as a long SMS.  
# SMS containing more than 70 Unicode characters, is automatically split as a long SMS.
# Information about split SMSes are sent to the url and are also reported in the Message Logs in the Account Dashboard. 

response = client.messages.create(
    src="19183836434",  # Sender's phone number with country code
    dst=" 15107171878",  # Sender's phone number with country code
    # Long text in French.
    # text="Ce texte généré aléatoirement peut-être utilisé dans vos maquettes (webdesign, sites internet,livres, affiches...) gratuitement. Ce texte est entièrement libre de droit. N'hésitez pas à faire un lien sur ce site en utilisant l'image ci-dessous ou en faisant un simple lien texte",
    # Long text in English.
    text = "This randomly generated text can be used in your layout (webdesign , websites, books, posters ... ) for free. This text is entirely free of law. Feel free to link to this site by using the image below or by making a simple text link",
    url="http://foo.com/sms_status/",  # URL for callback
    method="GET",  # The method used to call the url
)
# Prints the complete response
print(response)