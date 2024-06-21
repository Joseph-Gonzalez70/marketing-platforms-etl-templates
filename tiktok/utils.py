# coding=utf-8
import json
import requests
import pandas as pd


from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse  # noqa


def build_url(path:str, query:str=""):
   """
   Build request URL
   path: Request path
   query: Querystring
   return: Request URL
   """
   scheme, netloc = "https", "business-api.tiktok.com"
   return urlunparse((scheme, netloc, path, "", query, ""))

def get(json_str, 
        access_token, 
        path):
   """Send GET request
   :param json_str: Args in JSON format
   :return: Response in JSON format
   """
   args = json.loads(json_str)
   query_string = urlencode({k: v if isinstance(v, string_types) else json.dumps(v) for k, v in args.items()})
   url = build_url(path, query_string)
   headers = {
       "Access-Token": access_token,
   }
   rsp = requests.get(url, headers=headers)
   return rsp.json()


def get_synch_report(metrics_list, 
                     data_level,
                     end_date,
                     order_type, 
                     order_field, 
                     page_size, 
                     start_date,
                     advertiser_id, 
                     service_type, 
                     lifetime,
                     report_type, 
                     page, 
                     dimensions_list, 
                     access_token, 
                     path):


   metrics = json.dumps(metrics_list)
   dimensions = json.dumps(dimensions_list)


   # Args in JSON format
   my_args = "{\"metrics\": %s, \"data_level\": \"%s\", \"end_date\": \"%s\", \"order_type\": \"%s\", \"order_field\": \"%s\", \"page_size\": \"%s\", \"start_date\": \"%s\", \"advertiser_id\": \"%s\", \"service_type\": \"%s\", \"lifetime\": \"%s\", \"report_type\": \"%s\", \"page\": \"%s\", \"dimensions\": %s}" % (metrics, data_level, end_date, order_type, order_field, page_size, start_date, advertiser_id, service_type, lifetime, report_type, page, dimensions)
   tiktok_data = get(my_args, access_token, access_token)
   return(tiktok_data)

def get_creative_report(access_token, 
                        advertiser_id, 
                        material_type,
                        info_fields_list =["material_id", "video_id", "image_id", "page_id"], 
                        lifetime = False, 
                        page = 1, 
                        page_size = 10,
                        path = "/open_api/v1.3/creative/report/get/"):
  # material_id_list = MATERIAL_ID
   info_fields = json.dumps(info_fields_list)
   # Args in JSON format
   my_args = "{\"advertiser_id\": \"%s\", \"material_type\": \"%s\", \"lifetime\": \"%s\", \"info_fields\": %s, \"page\": \"%s\", \"page_size\": \"%s\"}" % (advertiser_id, material_type, lifetime, info_fields, page, page_size)
   creative_tiktok_data = get(my_args, access_token, path)
   return(creative_tiktok_data)


def get_image_info(access_token, 
                   advertiser_id, 
                   page = 1, 
                   page_size = 10, 
                   PATH = "/open_api/v1.3/file/image/ad/search/"):
   # Args in JSON format
   my_args = "{\"advertiser_id\": \"%s\", \"page\": \"%s\", \"page_size\": \"%s\"}" % (advertiser_id, page, page_size)
   print(my_args)
   return(get(my_args, access_token, PATH))


def get_account_videos(access_token, 
                       advertiser_id, 
                       page = 1, 
                       page_size = 10, 
                       path = "/open_api/v1.3/file/video/ad/search/"):
   advertiser_id = advertiser_id
   page_size = page_size
   # Args in JSON format
   my_args = "{\"advertiser_id\": \"%s\", \"page\": \"%s\", \"page_size\": \"%s\"}" % (advertiser_id, page, page_size)
   return(get(my_args, access_token, path))


def get_video_info(access_token, 
                   advertiser_id, 
                   video_ids, 
                   path = "/open_api/v1.3/file/video/ad/info/"):
   # Args in JSON format
   my_args = "{\"advertiser_id\": \"%s\", \"video_ids\": \"%s\"}" % (advertiser_id, video_ids)
   return(get(my_args, access_token, path))

def get_spark_adds_page(access_token, 
                        advertiser_id, 
                        page = 1, 
                        page_size = 10, 
                        path = "/open_api/v1.3/tt_video/list/"):
   # Args in JSON format
   my_args = "{\"advertiser_id\": \"%s\", \"page\": \"%s\", \"page_size\": \"%s\"}" % (advertiser_id, page, page_size)
   return(get(my_args, access_token, path))
