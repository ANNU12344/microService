from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
import requests

def get_all_post(wix_site):
    access_token = get_token_from_db(wix_site)
      
    if not access_token:   
        app_logger.error(f'No access token found for store: {wix_site}')
        raise TokenNotFoundException

    url = f"https://www.wixapis.com/v3/posts"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix API to get all post for wix site: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    app_logger.info(f'Wix API Response: {response.json()}')
   

    if response.status_code == 200:
        post_data = response.json()
        return post_data
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve post from Shopify API. Status Code: {response.status_code}')
    return []





def get_post_by_id(wix_site, post_ids):
    access_token = get_token_from_db(wix_site)
    # access_token="OAUTH2.eyJraWQiOiJLaUp3NXZpeSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiYXBwSWRcIjpcIjdiMjA5Mzg0LWU2NTctNGI1OS1iOTJlLTU0ZTYxZDNmYWZlY1wiLFwiaW5zdGFuY2VJZFwiOlwiODUzNGU4MDEtMDEyMy00YmQ1LTk4YTgtYjBmNmZiNDczNjk5XCIsXCJzY29wZVwiOltcIkg0c0lBQUFBQUFBQS81MVkyM0xrS0F6OW9Vei9BMjNURGhWc3ZJQjdrbjJoVWx1cDJYbllxYW5OL0grdEFHRnpFVTVtbjlLeE1VaEhSMGNTUmxqdURMZFdMSk81M0FYLyt2QlZQRHRqbGVibU1tendZeFovTWl2VTRyWjFaSmJuNzFldHhtMndUbk0ydXBucjRaRXQxc0VxbHErNmFyYU1ZYzBESDlSOENhc3RQRFJzOEJ1YitIamtVdHk1Zm5FRDAxcHdUWnczcTFIY1hwelNJOWZtNFNxa0JMTXZsajI3U2F0dGRUTmJWM2ppQmppQ3RoUU80ZlFiUEswMFJmUHAzUFBDNmVoanRrcUw2L1g0bkczMlVXbEU4eUtNVzdtZWhiVjhkTmNYQjZZN3NSakxscUZqQlhwMVlBaEEyUU1HZG1lU2FlWjJPRXpDd3lTM0IvaCtBaE44YU9QUEZ6ZXJPM2ZBZ3JrVEJUYnVZUlBMeUo5cjlQTmpkelRBMUpFdlZqQnBDUERFY2xOQXVoRDhqQmVqWmplTDI2UEZiaFJtVU50aXFXaTNzVVM4RWFpL1h0Ly8vdjcyNytXZjF4K3YzOTdpR2NnZ3NkeVZHTGloUXFwV1c2T2RySEI2azl5a1Y4a2lLWXgxWWw0bG44Rm5tcGtudTZFYlBRaTZ3RTNjcnl4M3pqK0hCOEN1VGxRMTkzRXY4bEZNazdlOWp3Z0draUpSYTJwSStqMzRPU0RlYXlKRGM5OU1rWTBZczhqMncrTGJKbSt3cmNmY1BBeWIxbndaWUpWYXdGR0lBcVpJZkE3R3hpL2p1ZTdLaGljZ2dUOGJmaXpLaXBzWUdQTHhqNDJiVGw3bHZFYWYwN0tCeVdHVGZuTllTS0ZZc2ViRHZEa1NBd0VvZVVOclJFR205QTRzQUtSNGJmRWVqSERTcCswaWowaThHcmxsb2pBK2hBRXBtUXBOZ0dma2R5NFZhQ0RvT215b3ZReEdHeHdjcWllT3U0QnNxam5FQmhLY3IwcGJCMTh1dHBzWXJlREVDblFpZ2pFZE1oa3NLMDFCdzBjK1BLbk5sb1JLVDkxTnF6bFF0ZEFsajhHakdBRkRaN2FyR2JTSUtSVXp5elJJa1VKUlZLZ2owL0c1NDgrV2cwQkRZZ2d1UjlPY2p6d3MxU2xGaENndXU1OVZzTHp1OEZIQXp2Q1VydzcyZWlJVXJ4T0ZuQm9HN0VVZlptQk5HVkFmNGt4YVduMkR3cFNWaDE1WHNnREtkMkhFVlZMT2xZd3NxOGhIK2dxZmVodUVqeUNUN3NiTGNsTDJUa1dLdFEwTGtabEpUNVJHeUdqZWRsNVErcG9RYlNPVDgzT25TZHQzN1ZzMDMwcUY2bmtzYVozdFZIb2ZSMWdaczg5MGdDNERuYkV4Y09ncW9pUUF0NldhZ2tsZjF1MHFVZFBKYkdyazlYZHFRcERPUW5GZmYvNzg4djcyNjlmM0g5L2VVOGZSYTdkeStPS2ZBOEM2aFN6TFlzV1RYS3VqVjN2SDEyVkdxc2c3VU9rTmthcDU3aFdLQ0N3UjkxanJKaEtWbG4rTnVoay9lbWdsWmNoRHkreVdCd1dzWW1CaUlFV2JQWGhLeHFpNjFuM1VZTFR2VWNuUnhJcG12anRmTjE4TkRZZE1NUTNGZHlIdFZaOWN2WGY1QWVmVzBETlF2VjdLMTBhYXFlNjE5QzdEc2ZEcXRNaWZ6M2NQa0QwcnpJcFFtcm5idEx6TWJHRVRLYXJ3WkZVR1ZOM0FvNWw5MkVubDBIalZCYkI5Nm9Ka2syMXBVZXhUVjdYVDJmOGl0R3VYTlpvdUIyQmVqaEJnWXB0KzlTWmFiSElZL0tBU1VBMXpJSHN6ZHB6TmU3ZzBiNTBHUDFoS2JKMG9ZUWlPK3dib013ZEVMeExvb045UC9NU3BqdkxueEdaWFNCSzE4SXhHbmF5blVneWpRNVNoV29IaUZORmtKeUVINElBL0RHbGU3OU1uUXVpUHBKaEV3ZC9jajFsTU90a0pWTzYyM3pYb3hGQlVERUdrZWh6WUJ5azlxbUJGejdKZk9lRmFWV2lxa2dSbFVzejVGSlNKYU5VcjkwL3ZqSk5VUzlaSzZZbnB6WGoxQ2YrSVNoWVRtU2lPSHlwZ1VTbnFDRlRqZGdaQ1Bpb0ZPaEszUmJ0d1Fnb0ZxVzVaYmlvQTJ3UkNPdTAxT3E4ZU9OcWs0SVgzT0hxMDdYU2I3S21IREUxZWExbW5ZYWdOSXZUanJBa3ZTa1gvN2c4bkJidFBDaWZaV3RFcjE2Vkc4YkZZRXgxeHRXbk9wWmJSWWQ5d3dSaG1QT00vaThTNmZOWGlkKzRVOHN6QmdCUVhzYzNWQUVvT0VOQU40WElydG0wcmUvR1NBNGZZUjVVNmpaREN1K0xsUFVqalVhNWtiSnloNnk0dWVVNlFPcW1QcDNjZi9lWUcwNjI2c2ZpL04wU1ZlcHgzZmJVZzByT1BlUlJodDg5T0syVVNvbUFVNHAvNXlhUXN1dkx3a0xwcHdsU3ZiM0pJWlVzM0xiR0U0bmpKL0pWa2VORFNqTGpLRGNZZFRVSERpL0pxdnBIQTl1SzRWd2k2QXo1ZVFkZnkwaTZNc3hZNmkvM0MwUnZCaVBSZzFSUEhvcXIwSmZ1UC93Y3NwZ3B2Z1JrQUFBPT1cIl0sXCJleHRyYUF0dHJpYnV0ZXNcIjp7XCJ3aXgtZ3ppcHBlZC1zY29wZVwiOlwiXCJ9fSIsImlhdCI6MTcxNTc2MjM1NSwiZXhwIjoxNzE1NzYyNjU1fQ.nAPZPGOo3dUONd_buQen3BYzxbT8m4EEplFDGrt6JDwQTPlny-EQ50n1L3kmGQlzHCJt_LN6C-TXMYL8oNHpafLVy6v0wz6f__J7zAm8MM3c0TG8QDewmMiqeGey1Z0fQddIFWCVUdATgqjhWS8oHz9gDHFH9vGF8wIXvId-3wk7QUe2ne8HjR-xnCly0uacK4JV3rrE9KiAOo2HtlMwX_ZQz5JT50e2Nv-NeT87Wn6lZaxpyySsX0uQY3MZqLfSnw5cWiujlgKiTU2Q36IUH7iGeY_HUGEY_9JcbLGK_Z00znjWYGSCUjISelLHgDvDe5oHNCB42gVp432cKsyoYQ"
    if not access_token:   
        app_logger.error(f'No access token found for wix site: {wix_site}')
        raise TokenNotFoundException

    
    url = f"https://www.wixapis.com/v3/posts/{post_ids}"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix API to get post with ID: {post_ids} for store: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        app_logger.info(f'Retrieved post with ID {post_ids} from wix API')
        app_logger.info(f'Response of post data:{response.json()}')
        post_data = response.json()
        return post_data
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve post with ID {post_ids[0]} from Wix API. Status Code: {response.status_code}')
    
    return response