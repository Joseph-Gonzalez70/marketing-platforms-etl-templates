import time
import datetime as dt
import pandas as pd
import numpy as np
import os
from tiktok.account import gettik_tok_accounts
from tik_tok_api_calls import tik_tok_api_pull


from dotenv import load_dotenv
load_dotenv()


# Get the TikTok API credentials
tiktok_access_token = os.getenv("TIKTOK_ACCESS_KEY")


# Set an object to store the data:
#ENTER HERE AN OBJECT TO STORE THE DATA

# Example for DOMO:
#domo_access_object = **json.loads(os.getenv("DOMO_CREDENTIALS"))
#domo = pydomo.Domo(domo_access_object['client_id'],domo_access_object['secret'], domo_access_object['api_host'])


# Pull the available Tiktok account ids
tiktok_account_names = pd.DataFrame(tik_tok_accounts.get_tiktok_accounts())
tiktok_account_names['advertiser_id'] = (
    tiktok_account_names['advertiser_id']
    .apply(lambda item: str(item))
)
tt_account_ids = tiktok_account_names['advertiser_id']


# Set the days we want to capture:
start_date = dt.date.today() - dt.timedelta(days=30)
end_date= dt.date.today()


campaign_data = pd.Series(dtype='float64')
for acc_id in tt_account_ids:
   time.sleep(2)
   tiktok_data = tik_tok_api_pull.get_synch_report(
                   metrics_list=,
                   data_level = 'AUCTION_CAMPAIGN',
                   end_date=end_date,
                   order_type='ASC',
                   order_field="impressions",
                   page_size = 500,
                   start_date = start_date,
                   advertiser_id = acc_id,
                   service_type='AUCTION',
                   lifetime=False,
                   report_type = 'BASIC',
                   page = 1,
                   dimensions_list = ["campaign_id", "stat_time_day"],
                   ACCESS_TOKEN = tiktok_access_token,
                   PATH = "/open_api/v1.3/report/integrated/get/")
   if 'list' in tiktok_data['data'].keys():
       tiktok_data_list = tiktok_data['data']['list']
   else:
       continue


   for list_item in tiktok_data_list:
       level_id_time = pd.Series(list_item['dimensions'])
       level_metrics = pd.Series(list_item['metrics'])
       data_row = pd.concat([level_id_time, 
                             level_metrics, 
                             pd.Series({"advertiser_id":acc_id, "batch_time": dt.datetime.now()})])
       campaign_data  = pd.concat([campaign_data, data_row], axis = 1)


# Transpose the data:
campaign_data =  campaign_data.transpose()
#if len(level_data) <= 10:
  # raise Exception("Date provided can't be in the past")
campaign_data = campaign_data.reset_index(drop = True)
campaign_data = campaign_data.dropna(how='all')
campaign_data.loc[:, "stat_time_day"] = (
    campaign_data.loc[:, "stat_time_day"]
    .apply(lambda item: re.search(r'[^ ]*', item).group())
)


# Convert data types:
numeric_data = (
    campaign_data
    .loc[:, [i for i in campaign_data.columns if i not in ("campaign_name",
                                                           "objective_type",
                                                           "app_promotion_type",
                                                           "currency", 
                                                           "campaign_id", 
                                                           "stat_time_day",
                                                           "secondary_goal_result", 
                                                           "batch_time", 
                                                           "advertiser_id")]]
    .astype("float32")
)

categorical_data = (
    campaign_data
    .loc[:, [i for i in campaign_data.columns if i in ("campaign_name",
                                                       "objective_type",
                                                       "app_promotion_type", 
                                                       "currency",
                                                       "campaign_id", 
                                                       "stat_time_day",
                                                       "secondary_goal_result", 
                                                       "advertiser_id", 
                                                       "batch_time")]]
)


tiktok_campaign_data = pd.concat([categorical_data , numeric_data], axis = 1)


# Add the account names:
tiktok_campaign_data = tiktok_campaign_data.merge(tiktok_account_names, 
                                                  how = 'left', 
                                                  on = 'advertiser_id' 
                                                )

# ***The following code is specificall for DOMO***

#temp_data = pd.Series(dtype='float64')
#temp_data = pd.concat([temp_data, tiktok_campaign_data], ignore_index = True)
#tiktok_campaign_data = temp_data


# Add the domo grab to get into unique date times
# Only need the recent pulling and keep the old static
#domo_tiktok_data = domo.ds_get("")
#domo_tiktok_data = domo_tiktok_data.dropna(how='all')
#domo_tiktok_data.loc[:, 'campaign_id'] = domo_tiktok_data.loc[:,'campaign_id'].apply(lambda item: str(np.int64(item)))
#domo_tiktok_data.loc[:,'advertiser_id'] = domo_tiktok_data.loc[:,'advertiser_id'].apply(lambda item: str(np.int64(item)))
#domo_tiktok_data['stat_time_day'] = domo_tiktok_data.loc[:, 'stat_time_day'].apply(lambda item: re.search(r'[^ ]*', str(item)).group())
#domo_tiktok_data = tiktok_campaign_data.merge(tik_tok_account_names , how = 'left', on = 'advertiser_id' )
#domo_tiktok_data = domo_tiktok_data.assign(batch_time = '2023-04-01 20:28:52.096486')
#domo_tiktok_data = domo_tiktok_data.loc[:, [i for i in domo_tiktok_data if i != 'row_num']]


#tiktok_full = pd.concat([tiktok_campaign_data, domo_tiktok_data], ignore_index = True)
#tiktok_full['row_num'] = tiktok_full.sort_values(["campaign_id", "stat_time_day", "batch_time"], \
                           #ascending=[True, True, False])\
                           #.groupby(["campaign_id", "stat_time_day"])\
                          # .cumcount() + 1
#domo_tiktok_data_final = tiktok_full.loc[tiktok_full.row_num == 1, [i for i in tiktok_full.columns if i != 'row_num']]




#domo.ds_update("", domo_tiktok_data_final)


