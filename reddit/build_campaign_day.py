import pandas as pd
import praw
from datetime import datetime
import json
import time
import pydomo
from Domo import domo_credentials as domo_cred
from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse  # noqa
from get_reddit_credentials import get_new_refreshed_access_token, get_username_password
import requests


#Connect to Domo:
#domo_access_fields = domo_cred.get_domo_creds()
#domo = pydomo.Domo(domo_access_fields[0], domo_access_fields[1], domo_access_fields[2])


# Reddit API credentials
test = get_new_refreshed_access_token()
client_id = ""
app_secret = ""
access_token = get_new_refreshed_access_token().json()['access_token']
username = get_username_password()['username']
password = get_username_password()['password']


headers = {'Content-Type': 'application/json',
          'Authorization': f"bearer {access_token}",
          'grant_type': 'authorization_code',
           'username': username,
           'password': password
}


# Accounts: 
accounts = ['', '', '']
account_data = pd.DataFrame()
for i in accounts:
   response = (
       requests.get(f"https://ads-api.reddit.com/api/v2.0/accounts/{i}",headers=headers)
       .json()
   )
   acc_temp = pd.Series(response['data'])
   account_data = pd.concat([account_data, acc_temp], axis=1)


account_data  = account_data.transpose()


domo.ds_create(account_data , 'base_reddit_ads_accounts')
######--------------------------------------------------------------------------------------------------------------------
# Get Campaigns
campaign_data = pd.DataFrame()
for i in accounts:
   time.sleep(1)
   response = (requests
               .get(f"https://ads-api.reddit.com/api/v2.0/accounts/{i}/campaigns", headers=headers)
               .json()
   )
   camp_temp = pd.DataFrame(response['data'])
   campaign_data = pd.concat([campaign_data, camp_temp], axis=0, ignore_index = True)


domo.ds_create(campaign_data, 'base_reddit_ads_campaigns')


#--------------------------------------------------------------------------------------------------------------------------------------------
# Reporting
parameters = {'ends_at': str(datetime.utcnow().strftime('%Y-%m-%dT%H')) + ':00:00Z',
           'group_by': ['campaign_id', 'date']                  ,
           'starts_at': '2022-01-01T00:00:00Z',
           }


reporting_data = pd.DataFrame()
for i in accounts:
   time.sleep(5)
   response = (
       requests
       .get(f"https://ads-api.reddit.com/api/v2.0/accounts/{i}/reports", headers=headers, params = parameters)
       .json()
   )
   report_temp = pd.DataFrame(response['data'])
   reporting_data = pd.concat([reporting_data, report_temp], axis=0, ignore_index = True)


string_columns = [i for i in reporting_data.columns if "custom" not in i
                                                       and  "legacy" not in i
                                                       and i not in ("app_install_metrics",
                                                                     "page_visit",
                                                                     "view_content",
                                                                     "view_content",
                                                                     "search",
                                                                     "add_to_cart",
                                                                     "add_to_wishlist",
                                                                     "purchase",
                                                                     "lead",
                                                                     "sign_up")]


reporting_data = reporting_data.loc[:, string_columns]


#domo.ds_create(reporting_data, 'reddit_ads_campaigns_day')
domo.ds_update('', reporting_data)
