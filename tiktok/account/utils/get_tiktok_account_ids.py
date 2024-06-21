# coding=utf-8
import json
from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse  # noqa
import requests
import os
import dotenv import load_dotenv
load_dotenv()

# Environment Variables
PATH = "/open_api/v1.3/oauth2/advertiser/get/"
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
APP_SECRET = os.environ.get('APP_SECRET')
APP_ID = os.environ.get('APP_ID')


def build_url(path: str, query: str = "") -> str:
   """
   Build request URL
   path: Request path
   query: Querystring
   return: Request URL
   """
   scheme, netloc = "https", "business-api.tiktok.com"
   return urlunparse((scheme, netloc, path, "", query, ""))


def get(json_str:str):
       # type: (str) -> dict
       """
       Send GET request
       json_str: Args in JSON format
       return: Response in JSON format
       """
       args = json.loads(json_str)
       query_string = urlencode({k: v if isinstance(v, string_types) else json.dumps(v) for k, v in args.items()})
       url = build_url(PATH, query_string)
       headers = {
           "Access-Token": ACCESS_TOKEN,
       }
       rsp = requests.get(url, headers=headers)
       return rsp.json()


def get_tiktok_accounts():
   access_token = ACCESS_TOKEN
   secret = APP_SECRET
   app_id = APP_ID


   # Args in JSON format
   my_args = "{\"access_token\": \"%s\", \"secret\": \"%s\", \"app_id\": \"%s\"}" % (access_token, secret, app_id)
   return(get(my_args)['data']['list'])