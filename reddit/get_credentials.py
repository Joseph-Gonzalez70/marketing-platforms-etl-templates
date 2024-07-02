# https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=code&state=RANDOM_STRING&redirect_uri=REDIRECT_URL&duration=DURATION&scope=SCOPE_STRING
#https://www.reddit.com/api/v1/authorize?client_id=pwg&response_type=code&state=93r&redirect_uri=https://www.___.com/&duration=permanent&scope=adsread,adsconversions,history
# redirect url: https://www.___.com/
# login code for access token:

# setup our header info, which gives reddit a brief description of our app
# In terminal:
#https://www.____.com/?state=9____d43r&code=j7_____Q#_


#curl -X POST https://www.reddit.com/api/v1/access_token -H 'content-type: application/x-www-form-urlencoded' -A 'media_app' -u pw7szg:5PYGCiw -d 'grant_type=authorization_code&code=j7OR0Q&redirect_uri=https://www.___.com/'


# Refresh Token:
#curl -X POST https://www.reddit.com/api/v1/access_token -A '_media_app' -u p6szg:Ciw -d 'grant_type=refresh_token&refresh_token=146Gj-M-Q'

# Refresh in python:
import requests


def get_new_refreshed_access_token():
   # Api Endpoint:
   url = 'https://www.reddit.com/api/v1/access_token'


   # Set the request headers
   headers = {
   'User-Agent': 'media_app',
   }


   # Set the client ID, app secret, and refresh token
   client_id = ''
   app_secret = ''
   refresh_token = ''


   # Set the request payload
   data = {
       'grant_type': 'refresh_token',
       'refresh_token': refresh_token,
           }
   # Set the authentication credentials
   auth = (client_id, app_secret)


   # Make the POST request
   response = requests.post(url, headers=headers, auth=auth, data=data)
   return(response)


def get_username_password():
   return({'username' : '', 'password' : ''})




#https://ads-api.reddit.com/docs/#section/Data-Freshness


#curl - X
#POST
#https: // www.reddit.com / api / v1 / access_token \ \
  # -H
#'content-type: application/x-www-form-urlencoded' \ \
  # -A
#'CLIENT_NAME' \ \
 #  -u
#CLIENT_ID: APP_SECRET \ \
  # -d
#grant_type=authorization_code&code=CODE&redirect_uri=REDIRECT_URL
