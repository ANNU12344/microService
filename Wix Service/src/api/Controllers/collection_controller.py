import json
import requests
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException
from src.Interactor.Dto.collection_dto import collection_dto
def createCollection(name:str):
    access_token="" #sset path to get the toekn
    if not access_token:
        app_logger.error(f'No access token found')
        raise TokenNotFoundException
    url = "https://www.wixapis.com/stores/v1/collections"
    payload = json.dumps({
        "collection": {
         "name": name
          }
         })
    headers = {
         'Content-Type': 'application/json',
        'Authorization': access_token
    }
    app_logger.info(f'Sending request to Wix api to create the collection with collection name :{name}')
    response = requests.request("POST",url, headers=headers, data=payload)
    app_logger.info(f'Wix API Response : {response.json()}')
    app_logger.info(f'Wix Api Response Status Code: {response.status_code}')
    if response.status_code==200:
        app_logger.info(f'Created Collection with collection Name:  {name }')
        return True
    if response.status_code==404:
        app_logger.warning(f'Error creating collection ')
        return False
    else:
        app_logger.warning(f'Failed to create the collection ')
        print(f'Error Creating the collection')
        return False
        
def get_collection_by_id(collection_id):
    app_logger.info(f'Received request to get the particular collection details with collection id {collection_id}')
    access_token = "OAUTH2.eyJraWQiOiJLaUp3NXZpeSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiYXBwSWRcIjpcIjU5ZWViYWQ3LWFkMTctNDMxNS1hOTdlLTNkNWY2NTIxZjQxMFwiLFwiaW5zdGFuY2VJZFwiOlwiMjliM2U2YTMtZDhmMi00NmRkLTk4Y2QtNThiYTU5ZThlMWMxXCIsXCJzY29wZVwiOltcIkg0c0lBQUFBQUFBQS81MVkyMjdjT0F6OW9lejhnOGJtZUlUSWxpdkprOHkrQ01FaWFQdXdSYkhwLzZQVXhiWXVsQ2ZkcDB4c1dTSVBEdzlKYVc3QWFqQ0dUNE0rM1RpOFBMM3dWNnVOVktCUDNZSS9SdjQzTTF4T2RwbDdaaUI5UHl2Wkw1MnhDbGh2UjFEZGxVM0c0aXFXcmpvck52Vit6Uk4wY2p6NTFRWWZhdGE1alhWNDNJUGdOMUIzMnpHbE9Daml2RkgyL0hLM1V2V2c5Tk9aQzRGbW53eDd0WU9TeTJ4SE5zLzR4SFo0QkcwcEhnTDBtM2hhYm9xQzRkanp6T25nWTdKSzhmTjUvNXd0NWlwVlJQUEV0WjFCamR3WTZPMzVidEYweXlkdDJOUTFySWhlN1JnaVVHYUhnZDJZWUlyWkRRNjk0cUZYdHp2OGZrQVRYR2pEejdzZDVRMHNzbUJzUklIMVc5ajQxTU5yaVg1NjdJWUdtdHJEWkRnVG1nQ1BUeGVKcFBQQlQzalJLM1l4Y2Z0b3NlMjU3dVF5R1NyYWRTd2ozaEdvZjk0K3ZuMS8vKy8wNzl1UHQ2L3Y0WXpJSUQ3ZEpPOUFVeUdWc3luUlhxMndhaEdnMTFlclJZSnJZL2s0Q3hqUlo1cVpCN3RGTjFvUU5JRWJ3SzNNZDA0L3h3Zklya1pVRmJpNFovbkloOEhaM2tZa0JwSWlVVzJxVC9vdCtDa2d6bXNpUTFQZmRKYU5NV2FCN2J2RmwwVmNjRnVIdVg3cUZxVmc2bkNWbk5CUmpFSk1rZkFjalExZmhuUHRtWFhQU0FKM052NllwT0VYM3JISXh5OEw2RVplcGJ5T1BxL0xPaWE2UmJqTmNTR0ZZc0dhaDNtekowWUVJT2NOclJFWm1kWjNhQUVpQmFYRld6RDhTWisyaXp4aTVWVVBodkhNZUIrR1NNbTEwSGg0ZXJpQmtLaUJxT3U0b1hJeUdHeXdlS2dhSU82Q3NpbEhIeHRNY0ppbE1oYS9uRXd6TVdyQkNSWG9RQVJET2lReW1GZWFqSVpYNko3bFluSkNyVS90UmNuUlV6WFRKWWZCbGZlSW9kWExXWGVLaDVRS21hVXJwRWlocVAzeVgwUis1YXF6SWswVWpjMytJZ2hPVDZEbnVETStoZG5pWHMrRWtqWFFUVU91WVlxT1lBWGlJZytVQzEwaUdiVnVZY0ZKWkw4MlBHZFJydnlQTkJFL2RmdHpoem9UOWdKNUNjajduU3d0NmlhRHlLWlZBNlNLY05CY3d4ZksyWWJTMVcvRWJxeW1oSEtGc0VHSVNMU05GM1VEdFcxUmZTdGtsTUY5U1kxQW8yUzd3T0hLa0VhNmdmNGUyWUorbmpSbkhuS2JUb0JLRWY5RXhyM2FaU0w1OXZQblh4L3Z2MzU5Ly9IMVkyMFNXaDFTQ2xUNHMwTlZkbjE1SlN0b2tzcHI4R3ByMHBvY2FLWmNta09aWW1IdytTM1Vvb0dFb0taVnBUN2FqUVpLQ3VGenpqQ3pwQkZBNDVpUWc0OTFuU254bElRb1pTMTYxQURVNzZQU1JoTUw5cmp1ZVY1Y3RkS0FDYUFyNW02QzJLb09hY2V4U1EwNk4vdWFUdlZpYXhwV0VrdDFsN2wzQ1k2WlY0ZEYrSGorZXNKVW1YR1d3OUlKZGxIaU5MS0pEWlR5dTg1d2xoclZXZU9qa1Qzc2RGSm9uTUlpMkFMejdJeGhwTnJHckJqWGNZeEUzZVNKNXNlT2tKT1ZpQ2l4VGJ1Y0VqMHZPWjA5a0htcWcvWHNydWFBb3dFc0xrMTdtYzVOZWlMMk1sVGFlOGRkUi9LWkF4NTQwWkRzbExyc2pHa2dKMGlJMHNocktvbGlPSWo2VVdwTTZPT3IvQ01TSGgxd2gwVWlsL3UwSSs4N0djRUhuakUwOVdQa2cxcnRSTEkyRytBU1pXSXN5Y1lRVWg5MjdMMVk3a1d0NEdQZWZSeVFxNmdiUllYQnFzZkhkQTVKWkxMb1Z0dW5Od1k2cXNHcXhmTEE5R3JBK1lSL1JLMEttVXVVdjRjYWw5V0NNZ0xGd0p1QWtBNHJubzdFZmMwbWpaaENYb3hybHVzQ3dEcUJJcDIyS3B6V2h6aGNyTUh6N3dNamllYTRUdmExK2ZQZFdXMVpveVVvRFNMMDQ2aWx6b3BCKy9iTkg0VU5uTDF4N2RMMktGc0xlcVc2VkVsOExNZEVLMXRzbW5LcFpyVGYxMS94d2F1QlNidlBBckZPTDRyL3lWU2ZaazRNU0hZVldnM25VWEtRZ0xiejEwdWhNWnZaM1VrT0htS3VjdTBsZkFwdmlwZDJHWlZIcVpLeGZzUW1PcnRtT1VEcW9DQWUzajYwMjVlWWJzV2R3Zis5b3luVTQ3aXZLd1dSSGxyMGxmdmRQanQ4NUVrWUJTTVQvOFJQSmtUV2QvdUgxRjFQVFBYeUxvVlV0dld1STVUUU9CY3lkeW5vSDlRMEl5NVR2WEY3VTFEeElyOGNyeVN3dnJwdEZZTG11QjR2Z1V0NXFSZUcwU2s2Ry9zRkk1OGhsbEdwVHNsLzhCdmlnUS81OVJnQUFBPT1cIl0sXCJleHRyYUF0dHJpYnV0ZXNcIjp7XCJ3aXgtZ3ppcHBlZC1zY29wZVwiOlwiXCJ9fSIsImlhdCI6MTcxNDM2MzIxNywiZXhwIjoxNzE0MzYzNTE3fQ.KBQQz59sNkYJcNglrPa766qnbyqmbOqz8dTAWNgSMlKDAag_2wgb9U_rxsWdcDpyJSCdp7vi3G-WUUVeASQWhBYp3sMh4Q8Krc8j5Yk1fzTv4MZipgyhKBGPXfdm0RW7f0Ocjs0ZWw_EBLvbipZ6qRZ3Gkn-s8an6bUF0ckaLEGXkBivXRUEXpWt2A-9zmgLB7hOAxWANQp3lYOYOvBZe9JEDVZXaPEfCH01d5tpmSRnwX6FtTgupVAlq1PZvbAlpZQ_5ZsJM4gcMS6g8N4jvK5vCIMogiwJR06AGaxyAWY4VgJNg42uxW_l33V-Lywhk_K8B1o0qXrbeceWrZTGsg"
    url = f"https://www.wixapis.com/stores/v1/collections/{collection_id}?includeNumberOfProducts=true"
    headers = {'Authorization': access_token}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        collection_data = response.json()
        app_logger.info(f'Successfully retrieved collection details: {collection_data}')
        return collection_data
    except requests.exceptions.RequestException as e:
        app_logger.error(f'Failed to retrieve collection details: {e}')
        return "Failed to retrieve collection details", 500
    