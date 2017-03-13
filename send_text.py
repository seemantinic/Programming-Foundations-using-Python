from twilio import rest

account_sid = "AC2e917c1bf4fff439f93462a6186b61e1" # Your Account SID from www.twilio.com/console
auth_token  = "d0f8af0f2a803d444eeeccbeebe164b1"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="I am awesome. hehehehe :-D",
    to="+19597772278",    # Replace with your phone number
    from_="+16144728261") # Replace with your Twilio number

print(message.sid)
