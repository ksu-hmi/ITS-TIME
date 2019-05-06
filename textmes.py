from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console so right now I have fake information in the ''
# DANGER! This is not a secure method. See http://twil.io/secure
# The from phone number is your phone number - prefer cell number
# The to phone number is the cell phone number that you want to send the message to

account_sid = 'xxxxxxxx'
auth_token = 'asdfjewifoej'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Enter any message inbetween the quotes that you want to send",
                     from_='+9999999999',
                     to='000000000'
                     
                 )

print(message.sid)
