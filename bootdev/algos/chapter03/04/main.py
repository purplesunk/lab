def get_avg_brand_followers(all_handles, brand_name):
    if not all_handles:
        return None
    brand_followers = 0
    list_number = len(all_handles)
    for list in all_handles:
        for follower in list:
            if brand_name in follower:
                brand_followers += 1
    return brand_followers / list_number
