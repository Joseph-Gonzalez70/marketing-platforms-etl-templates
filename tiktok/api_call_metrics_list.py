api_metrics_list = [
                   # Attribute metrics:
                   "campaign_name",
                   "objective_type",
                   "campaign_budget",
                   "split_test",
                   "campaign_dedicate_type",
                   "app_promotion_type" ,
                   # Basic Metrics
                   "spend",
                   "impressions",
                   "gross_impressions",
                   "clicks",
                   "reach",
                   "conversion",
                   "real_time_conversion",
                   "result",
                   "real_time_result",
                   "secondary_goal_result",
                   "frequency",
                   "currency",
                   # Video Plat Metric
                   "video_play_actions",
                   "video_watched_2s",
                   "video_watched_6s",
                   "video_views_p25",
                   "video_views_p50",
                   "video_views_p75",
                   "video_views_p100",
                   "engaged_view",
                   "engaged_view_15s",
                   # Engagement Metrics
                   "engagements", 
                   "profile_visits", 
                   "likes", 
                   "comments", 
                   "shares", 
                   "follows", 
                   "clicks_on_music_disc", 
                   "duet_clicks",
                   "stitch_clicks", 
                   "sound_usage_clicks", 
                   "anchor_clicks", 
                   "anchor_click_rate", 
                   "clicks_on_hashtag_challenge",
                   # Instant Experience
                   "ix_video_views", 
                   "ix_video_views_p25", 
                   "ix_video_views_p50", 
                   "ix_video_views_p75", 
                   "ix_video_views_p100",
                   # Interactive Add-on Metrics
                   "interactive_add_on_impressions", 
                   "interactive_add_on_destination_clicks", 
                   "interactive_add_on_activity_clicks",
                   "interactive_add_on_option_a_clicks", 
                   "interactive_add_on_option_b_clicks", 
                   "countdown_sticker_recall_clicks",
                   # Live broadcast metrics
                   "live_views", 
                   "live_unique_views", 
                   "live_effective_views", 
                   "live_product_clicks",
                   # In-App Event Metrics
                   "real_time_app_install", 
                   "app_install", 
                   "registration", 
                   "total_registration", 
                   "purchase", 
                   "total_purchase",
                   "total_purchase_value", 
                   "app_event_add_to_cart",
                   "total_app_event_add_to_cart", 
                   "total_app_event_add_to_cart_value",
                   "checkout", 
                   "total_checkout", 
                   "total_checkout_value", 
                   "view_content", 
                   "total_view_content", 
                   "total_view_content_value",
                   "next_day_open", 
                   "total_next_day_open", 
                   "add_payment_info", 
                   "total_add_payment_info", 
                   "add_to_wishlist",
                   "total_add_to_wishlist", 
                   "total_add_to_wishlist_value", 
                   "launch_app", 
                   "total_launch_app", 
                   "complete_tutorial", 
                   "total_complete_tutorial", 
                   "total_complete_tutorial_value", 
                   "create_group",
                   "total_create_group",
                   "total_create_group_value",
                    "join_group", 
                    "total_join_group", 
                    "total_join_group_value"
                    "create_gamerole", 
                    "total_create_gamerole", 
                    "total_create_gamerole_value",
                    "spend_credits", 
                    "total_spend_credits",
                    "total_spend_credits_value", 
                    "achieve_level", 
                    "total_achieve_level", 
                    "total_achieve_level_value", 
                    "unlock_achievement",
                    "total_unlock_achievement", 
                    "total_unlock_achievement_value", 
                    "sales_lead", 
                    "total_sales_lead", 
                    "total_sales_lead_value",
                    "in_app_ad_click", 
                    "total_in_app_ad_click", 
                    "total_in_app_ad_click_value", 
                    "in_app_ad_impr", 
                    "total_in_app_ad_impr",
                    "total_in_app_ad_impr_value", 
                    "loan_apply", 
                    "total_loan_apply", 
                    "loan_credit", 
                    "total_loan_credit", 
                    "loan_disbursement"
                    "total_loan_disbursement", 
                    "login", 
                    "total_login", 
                    "ratings", 
                    "total_ratings", 
                    "total_ratings_value", 
                    "search",
                    "total_search", 
                    "start_trial", 
                    "total_start_trial",
                    "subscribe", 
                    "total_subscribe", 
                    "total_subscribe_value",
                    "unique_custom_app_events", 
                    "custom_app_events",
                    "custom_app_events_value",
                   # Onsite
                    "onsite_shopping", 
                    "total_onsite_shopping_value", 
                    "onsite_initiate_checkout_count", 
                    "total_onsite_initiate_checkout_count_value",
                    "onsite_on_web_detail", 
                    "total_onsite_on_web_detail_value", 
                    "onsite_add_to_wishlist", 
                    "total_onsite_add_to_wishlist_value",
                    "onsite_add_billing", 
                    "total_onsite_add_billing_value", 
                    "onsite_on_web_cart", 
                    "total_onsite_on_web_cart_value", 
                    "onsite_form",
                    "total_onsite_form_value", 
                    "ix_page_view_count", 
                    "ix_button_click_count", 
                    "ix_product_click_count",
                   # Page Event Metrics
                    "complete_payment", 
                    "total_complete_payment_rate", 
                    "total_landing_page_view", 
                    "total_pageview", 
                    "total_value_per_pageview",
                   , "page_browse_view", "total_page_browse_view_value", "value_per_page_browse_view", "button_click" , "value_per_button_click"
                   , "total_button_click_value", "online_consult", "total_online_consult_value", "user_registration", "total_user_registration_value"
                   , "product_details_page_browse", "total_product_details_page_browse_value", "web_event_add_to_cart", "total_web_event_add_to_cart_value"
                   , "on_web_order", "total_on_web_order_value", "initiate_checkout", "total_initiate_checkout_value", "add_billing", "total_add_billing_value"
                   , "page_event_search", "total_page_event_search_value", "form", "total_form_value", "download_start", "total_download_start_value"
                   , "on_web_add_to_wishlist", "total_on_web_add_to_wishlist_value", "on_web_subscribe", "total_on_web_subscribe_value", "custom_page_events"
                   , "custom_page_events_value"
                   # Attribution Metrics
                   , "vta_app_install", "vta_conversion", "vta_registration", "vta_purchase"
                   , "cta_app_install", "cta_conversion", "cta_registration", "cta_purchase"
                   # Offline Metrics
                   , "offline_shopping_events", "offline_shopping_events_value", "offline_contact_events", "offline_contact_events_value"
                   , "offline_subscribe_events", "offline_subscribe_events_value", "offline_form_events", "offline_form_events_value"
                   # SKAN Metrics
                   #, "skan_result", "skan_cost_per_result", --> Not supported by campaigns
                   , "skan_conversion", "skan_click_time_conversion"
                   # In-App Event metrics (SKAN)
                   , "skan_app_install", "skan_app_install_withheld", "skan_registration", "skan_total_registration"
                   , "skan_purchase", "skan_total_purchase", "skan_total_purchase_value", "skan_add_to_cart"
                   , "skan_total_add_to_cart", "skan_total_add_to_cart_value", "skan_checkout", "skan_total_checkout", "skan_total_checkout_value"
                   , "skan_view_content", "skan_total_view_content", "skan_total_view_content_value", "skan_add_payment_info", "skan_total_add_payment_info"
                   , "skan_add_to_wishlist", "skan_total_add_to_wishlist", "skan_total_add_to_wishlist_value", "skan_launch_app"
                   , "skan_total_launch_app", "skan_total_complete_tutorial", "skan_complete_tutorial", "skan_total_complete_tutorial_value"
                   , "skan_create_group", "skan_total_create_group", "skan_total_create_group_value", "skan_join_group", "skan_total_join_group"
                   , "skan_total_join_group_value", "skan_create_gamerole", "skan_total_create_gamerole", "skan_total_create_gamerole_value"
                   , "skan_spend_credits", "skan_total_spend_credits", "skan_total_spend_credits_value", "skan_achieve_level"
                   , "skan_total_achieve_level", "skan_total_achieve_level_value", "skan_unlock_achievement", "skan_total_unlock_achievement"
                   , "skan_total_unlock_achievement_value", "skan_sales_lead", "skan_total_sales_lead", "skan_total_sales_lead_value"
                   , "skan_in_app_ad_click", "skan_total_in_app_ad_click", "skan_total_in_app_ad_click_value"
                   , "skan_in_app_ad_impr", "skan_total_in_app_ad_impr", "skan_total_in_app_ad_impr_value", "skan_loan_apply", "skan_total_loan_apply"
                   , "skan_loan_credit", "skan_total_loan_credit", "skan_cost_per_total_loan_credit", "skan_loan_disbursement", "skan_total_loan_disbursement"
                  #, "skan_login", "skan_total_login", "skan_ratings", "skan_total_ratings", "skan_total_ratings_value", "skan_search"
                  # , "skan_total_search", "skan_start_trial", "skan_total_start_trial", "skan_subscribe", "skan_total_subscribe", "skan_total_subscribe_value"
                 # Attribution metrics (SKAN)
                 #  , "skan_vta_conversion", "skan_vta_app_install","skan_cost_per_vta_app_install",  "skan_vta_registration"
                  ]