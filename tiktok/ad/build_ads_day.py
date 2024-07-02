import time
#import pydomo
import datetime as dt
import pandas as pd
#import numpy as np
import re
import os
from tiktok.account.utils.get_tiktok_account_ids import get_tiktok_accounts
import utils 
from api_call_metrics_list import api_metrics_list


from dotenv import load_dotenv
load_dotenv()


# Get the TikTok API credentials
tiktok_access_token = os.getenv("TIKTOK_ACCESS_TOKEN")

# Set an object to store the data:
#ENTER HERE AN OBJECT TO STORE THE DATA

# Example for DOMO:
#domo_access_object = **json.loads(os.getenv("DOMO_CREDENTIALS"))
#domo = pydomo.Domo(domo_access_object['client_id'],
# domo_access_object['secret'], 
# domo_access_object['api_host'])


# Pull the Tiktok account ids
tik_tok_account_names = pd.DataFrame(get_tiktok_accounts())
tik_tok_account_names['advertiser_id' ] = (
    tik_tok_account_names['advertiser_id']
    .apply(lambda item: str(item))
)
tt_account_ids =  tik_tok_account_names['advertiser_id']


# Set the days we want to capture:
start_date = dt.date.today() - dt.timedelta(days=30)
end_date = dt.date.today()




ad_data = pd.Series(dtype='float64')
for acc_id in tt_account_ids:
   time.sleep(2)
   tiktok_data = utils.get_synch_report(
                   metrics_list=api_metrics_list,
                   data_level = 'AUCTION_AD',
                   end_date=end_date,
                   order_type='ASC',
                   order_field="impressions",
                   page_size = 1000,
                   start_date = start_date,
                   advertiser_id = acc_id,
                   service_type='AUCTION',
                   lifetime=False,
                   report_type = 'BASIC',
                   page = 1,
                   dimensions_list = [ "ad_id", "stat_time_day"],
                   ACCESS_TOKEN = tiktok_access_token, 
                   PATH = "/open_api/v1.3/report/integrated/get/")
   if 'list' in tiktok_data['data'].keys():
       data_list = tiktok_data['data']['list']
   else:
       print('here')
       continue


   for list_item in data_list:
       level_id_time = pd.Series(list_item['dimensions'])
       level_metrics = pd.Series(list_item['metrics'])
       data_row = pd.concat([level_id_time, 
                             level_metrics, 
                             pd.Series({"advertiser_id":acc_id, "batch_time": dt.datetime.now()})]
                            )
       ad_data = pd.concat([ad_data , data_row], axis = 1)


ad_data = ad_data.transpose()


#if len(ad_data) <= 10:
   #raise Exception("Date provided can't be in the past")
ad_data = ad_data.reset_index(drop = True)
ad_data = ad_data.dropna(how='all')
ad_data.loc[:, "stat_time_day"] = (
    ad_data.loc[:, "stat_time_day"]
    .apply(lambda item: re.search(r'[^ ]*', item).group())
)


# Convert data types:
ad_data["bid"].replace('-', None)
numeric_data = (
   ad_data
   .loc[:,
       [i for i in ad_data.columns if i not in ("campaign_name",
                                               "objective_type",
                                               "app_promotion_type",
                                               "currency",
                                               "campaign_id",
                                               "stat_time_day",
                                               "secondary_goal_result",
                                               "advertiser_id",
                                               "batch_time",
                                               "adgroup_name",
                                               "adgroup_id",
                                               "placement_type",
                                               "bid",
                                               "promotion_type",
                                               "dpa_target_audience_type",
                                               "smart_target",
                                               "pricing_category",
                                               "bid_strategy",
                                               "aeo_type",
                                               "ad_name",
                                               "ad_text",
                                               "call_to_action",
                                               "tt_app_id",
                                               "tt_app_name",
                                               "mobile_app_id",
                                               "bid_strategy",
                                               "app_promotion_type",
                                               "secondary_goal_result",
                                               "objective_type",
                                               "dpa_target_audience_type",
                                               "aeo_type",
                                               "call_to_action",
                                               "ad_id")
                                           ]
                                       ]
   .astype("float32")
)
categorical_data = (
   ad_data
   .loc[:, [i for i in ad_data.columns if i in ("campaign_name",
                                               "objective_type",
                                               "app_promotion_type",
                                               "currency",
                                               "campaign_id",
                                               "stat_time_day",
                                               "secondary_goal_result",
                                               "advertiser_id",
                                               "batch_time",
                                               "adgroup_name",
                                               "adgroup_id",
                                               "placement_type",
                                               "bid",
                                               "promotion_type",
                                               "dpa_target_audience_type",
                                               "smart_target",
                                               "pricing_category",
                                               "bid_strategy",
                                               "aeo_type",
                                               "ad_name",
                                               "ad_text",
                                               "call_to_action",
                                               "tt_app_id",
                                               "tt_app_name",
                                               "mobile_app_id",
                                               "bid_strategy",
                                               "app_promotion_type",
                                               "secondary_goal_result",
                                               "objective_type",
                                               "dpa_target_audience_type",
                                               "aeo_type",
                                               "call_to_action",
                                               "ad_id")
                                               ]
                                           ]
)




tiktok_ad_data = pd.concat([categorical_data , numeric_data], axis = 1)


# Get the account names:
tiktok_ad_data= tiktok_ad_data.merge(tik_tok_account_names , how = 'left', on = 'advertiser_id' )


# ADD WHEN NEEDING TO BACKFILL OR ADD NEW COLUMNS ************************************************************
#temp_data = pd.Series(dtype='float64')
#temp_data= pd.concat([tiktok_ad_data, temp_data], ignore_index = True)
# tiktok_ad_data = temp_data
#domo.ds_update('', temp_data)


# Add the domo grab to get into unique date times
# Only need the recent pulling and keep the old static
#domo_tiktok_data = domo.ds_get('')
#domo_tiktok_data = domo_tiktok_data.dropna(how='all')
#domo_tiktok_data.loc[:, 'ad_id'] = (
#   domo_tiktok_data
#   .loc[:,'ad_id']
#   .apply(lambda item: str(np.int64(item)))
#)
#domo_tiktok_data.loc[:,'advertiser_id'] = (
  # domo_tiktok_data
  # .loc[:,'advertiser_id']
  # .apply(lambda item: str(np.int64(item)))
#)
#domo_tiktok_data['stat_time_day'] = (
  # domo_tiktok_data.loc[:, 'stat_time_day']
  # .apply(lambda item: re.search(r'[^ ]*', str(item)).group())
#)

#tiktok_full = pd.concat([tiktok_ad_data, domo_tiktok_data], ignore_index = True)
#tiktok_full['row_num'] = (tiktok_full.sort_values(["ad_id", "stat_time_day", "batch_time"],
                       #    ascending=[True, True, False])
                       #    .groupby(["ad_id", "stat_time_day"])
                       #    .cumcount() + 1
#)
#domo_tiktok_ad_data = (
# tiktok_full
# .loc[tiktok_full.row_num == 1, [i for i in tiktok_full.columns if i != 'row_num']]



#domo.ds_create(tiktok_ad_data, 'base_tik_tok_ads_day')


#domo.ds_update('', domo_tiktok_ad_data)
