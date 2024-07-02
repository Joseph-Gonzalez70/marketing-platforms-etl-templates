import json
import pandas as pd
import time
#import pydomo
#from venv.Domo import domo_credentials as domo_cred
import os
from api_call_metrics_list import api_metrics_list

from tiktok.utils import get, post
from tiktok.account.utils.get_tiktok_account_ids import get_tiktok_accounts

from dotenv import load_dotenv
load_dotenv()

# Set Environment Variables:
ACCESS_TOKEN = os.environ.get('TIKTOK_ACCESS_TOKEN')
PATH = "/open_api/v1.3/report/task/create/"

# Connect to Data Warehouse:
# domo_access_fields = domo_cred.get_domo_creds()
# domo = pydomo.Domo(domo_access_fields[0], domo_access_fields[1], domo_access_fields[2])


# Get the current data from the Data Warehouse:
# tt_campaigns = domo.ds_get('')
# tt_account_ids =  tt_campaigns['advertiser_id'].unique()
# tt_account_ids =  tt_account_ids.astype(str)

# Get the TikTok account ids:
tiktok_account_names = pd.DataFrame(get_tiktok_accounts())
tiktok_account_names['advertiser_id'] = (
    tiktok_account_names['advertiser_id']
    .apply(lambda item: str(item))
)
tt_account_ids = tiktok_account_names['advertiser_id']

# Set the parameters for the report:
task_ids = [] # Collect the task ids to download the reports
for advertiser in tt_account_ids:
    advertiser_id = advertiser
    data_level = "AUCTION_CAMPAIGN"
    report_type = "BASIC"
    dimensions_list =["campaign_id", "stat_time_day"]
    dimensions = json.dumps(dimensions_list)
    metrics_list = api_metrics_list
    metrics = json.dumps(metrics_list)
    order_type = 'ASC'
    order_field = "impressions"
    start_date = ""
    end_date = ""
    service_type='AUCTION'
    output_format = "CSV_DOWNLOAD"
    file_name = "account_" + advertiser + start_date + "_to_" + end_date
    #filter_value=0
    # #field_name = "impressions"
    # #filter_type='GREATER_EQUAL'
    # Args in JSON format
    my_args = "{\"metrics\": %s, \"data_level\": \"%s\", \"end_date\": \"%s\", \"order_type\": \"%s\", \"order_field\": \"%s\", \"output_format\": \"%s\",  \"start_date\": \"%s\", \"advertiser_id\": \"%s\", \"service_type\": \"%s\", \"report_type\": \"%s\",  \"dimensions\": %s}" % (metrics, data_level, end_date, order_type, order_field, output_format, start_date, advertiser_id, service_type, report_type, dimensions)
    task_ids.append(post(my_args))
    time.sleep(20)

time.sleep(30)

# Status of Report:
is_success = []
task_ids = [i['data']['task_id'] for i in task_ids]
tasks_accounts_ids = zip(task_ids,tt_account_ids)
PATH = "/open_api/v1.3/report/task/check/"
for t_id, advertiser in tasks_accounts_ids:
    my_args = "{\"advertiser_id\": \"%s\", \"task_id\": \"%s\"}" % (advertiser, t_id)
    is_success.append(get(my_args)['data']['status'])

# Get the download links:
tasks_accounts_ids = zip(task_ids,tt_account_ids)
PATH = "/open_api/v1.3/report/task/download/"
download_links = []
for t_id, advertiser in tasks_accounts_ids:
    task_id = t_id
    # Args in JSON format
    my_args = "{\"advertiser_id\": \"%s\", \"task_id\": \"%s\"}" % ('', '')
    download_links.append(get(my_args)['data']['download_url'])

# Save list in a text file:
with open('download_links.txt', 'w') as f:
    for item in download_links:
        f.write("%s\n" % item)

# Download the report:
for id, link in zip(tt_account_ids, download_links): #download_links, download_links:
    df = pd.read_csv(link)
    df.save_csv('account_' + id + '.csv')


