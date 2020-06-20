from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "hey shreeda bhat, we heard that you have been enrolling in www.udemy.com...we are intrested in you to offrer campus ambaseder intern role,so kindly call us!!"

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
