import requests
from src.Interactor.Logger.custom_logger import app_logger
import json
def createProduct(name,id,visible,productType,description,slug,weight):
    url=f"https://www.wixapis.com/stores/v1/products"
    access_token=" "#I have to set this like how to get the token from the database
    product={
        "name":name,
        "id":id,
        "visible":visible,
        "productType":productType,
        "description":description,
        "slug":slug,
        "weight":weight
    }
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token,
    }
    response = requests.post(url, headers=headers, data=json.dumps(product))
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        print(response.json())


def get_product_by_id(product_id):
    app_logger.info(f'Received request to get the particular collection details with product id {product_id}')
    access_token = " "
    url = f"https://www.wixapis.com/stores-reader/v1/products/{product_id}"
    headers = {'Authorization': access_token}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        product_data = response.json()
        app_logger.info(f'Successfully retrieved product details: {product_id}')
        return product_data
    except requests.exceptions.RequestException as e:
        app_logger.error(f'Failed to retrieve product details: {e}')
        return "Failed to retrieve product details", 500
    

def get_Product_Options_Availability(product_id,optionType,Name):
    app_logger.info(f'Received request to check the product availability with optionType :{optionType} and Name :{Name}')
    access_token = "OAUTH2.eyJraWQiOiJLaUp3NXZpeSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiYXBwSWRcIjpcIjU5ZWViYWQ3LWFkMTctNDMxNS1hOTdlLTNkNWY2NTIxZjQxMFwiLFwiaW5zdGFuY2VJZFwiOlwiMjliM2U2YTMtZDhmMi00NmRkLTk4Y2QtNThiYTU5ZThlMWMxXCIsXCJzY29wZVwiOltcIkg0c0lBQUFBQUFBQS81MVkyM0xjS0JEOUllLzhBeU14R3NwSUtJREdubjJoWEZ1dUpBK2JTcTN6LzVVR1doS1hSdVBzazhjU2dyNmNjN29iSXl4M2hsc3Jwc0djYm9LL1BMMklWMmVzMHR5Y3VnVitqT0p2Wm9XYTNETDN6UEwwL2F4VnYzVFdhYzU2TjNMZFhkbGtIYXhpNmFxelpsTWYxanp4VG8ybnNOckNROE02djdHSmozc3V4WTNydSt1WTFvSnI0cnhSOWVKeWQwcjNYSnVuczVBU3pENVo5dW9HclpiWmpXeWU0WW5yNEFqYVVqaUUwMi93dE53VXpZZGp6ek9ubzQvSktpM081LzF6dHRpcjBoak5rekJ1NW5vVTF2TGVuZThPVEhkaU1wWk5YY01LOUdxUElRVEs3bUZnTnlhWlptNExoMW5qWVZhM08vaCtBQk44YXVQUHV4dlZqVHRBd2RqSUF1dTN0SW1wNTY5bDlOTmp0MmlBcVQyZnJHRFNFTUVUMDBVQjZFTHlFMXowbWwwc2JvOFd1MTZZVGkyVHBiSmQ1eExqallINjUrM2oyL2YzLzA3L3Z2MTQrL29lejBBRWllbW1STWNObFZJMTJ6TGFxeFZPTDVLYjlkVnFrUlRHT2pIT2tvL2dNNDNNZzkzUWpWWUltb0VidUYrWjc1eCtEZzhBWFkyc2F1N3pudkZSRElPM3ZSMFJUQ1FGb3RyVVFQb3QrV2xBdk5jRVExUGZUTVpHekZsRSsyN3haWkVYMk5iSDNEeDFpOVo4Nm1DVm1zQlJ5QUpTSkQ0SFkrT1g4VngzWnQwemdNQ2ZEVDhtWmNWRmRBengrR1hocHNHckZOZm84N3FzWTdKYnBOOGNGbEpSTEZEemtEYzdNVEFBT1c1b2pjakF0TDREQ3lCU3ZMUjRTMFk0NmROMmtVZXN1T3E1WlNJelBxUUJJYmtXbWhDZW50KzRWS0NCb091d29mWXlHRzF3Y0tnZU9PNENzcW5Ha0JzZ09KK1Z0ZzYrbkd5VEdMWGd4QXAwSUlLUkRva001cFVtZytHVmQ4OXFzVG1nMXFmdW90VVlvSnJwa28vQlZmUVFRMmVXcyttMGlKU0t6REpWcEVpaHlDclV6blI4N3ZpcjVTRFFRQXpCWlcrcTh4R0h1VHF0R1NHS3krWm5rU3l2Tzd3WHNETTg1Yk9Edlo0SnhXdGtJWVdHQVh2Umh4RlFreWZVcHppUmxscmZvREFsNWFIVmxVd1E1WnN3NGl3cDUzSkU1bFhra2I3Q3A5NEc0VFBJcEx2d3ZKemt2Vk5Hc2JwaElaaTU2b25TR0RJYXQvQkNlOXRBQnZ1TkpJM1ZsT2l1WWE3VGxZSjJ3MDdkakcxYlZOOUtoWks2TDZrajBDai9Qcm13TWxMU05LS2ZaeitCYUFEV1dVU2RvTWxVcWV1ZmxJU2duSm5ndnYzOCtkZkgrNjlmMzM5OC9WZ2JqbGEzbFFZcS90bERWWGFRZVZVc1lKSktkZlJxYS9pYUdHalNNdVZacG42UWZIR0xkVzBnUTFERHFsSXk0OGNNcmFRTW5MUE1MbWtHd0RnbTFSQnlYVE1GVDBtQVV0YTFSODFFL1I1VkcwMHMwT003OFhueGxjOXdJSUNwa0x1SlpxdlNwRXE5U1EwNE40ZitnT3JyVmhwV01reDFxcmwzU1J3enJ3NEwrdkVzOXdSVW1XRXVoRExNM2FMbGFXUVRHMGdCaFNlek1xRGdCaDZON0dIWGxJYkdLeXdFV3dMUFFKN0pGalFyN0hVZUVhaWJQTkg0MkNQa1pRVWpTbXpUTHMxRS8weE9lZzlrbnVxR0E3cXJtZUpvbU1PbGFWL1UrYWxSWWw5RTBUNDQ3cnVienh6d3dJdUdaS2ZRWldlZ2dacDRBcFFHcnlrU1lUcUkrbEZxVEp3Skt2NFJoQWNIL0dFSTVIS2ZkdVpEdHlQRklES0VwbjZNWXRDcm5RRFdaak5kUnBrWWNiS1JodFNIUGZaQkxQZWlWdUF4N3o0T3dGWFVqYUxDUU5VVFl6clRKREpaZEw3dDB4dkRJZFZnMVdKNVlIbzFMSDNDUDZKV1JlWVM1ZStoeG1XMW9NeEFNVHduUVVnSG53Qkg0dTVuazBhZ1VCRGpHdVdtQ0dCTklJVFRWb1hUK29DRHlwcTg4QjRIaWJvNXJzbStObitoTzZzdGE3UUVwVUdFZmh5MTFGa3hhTi9rWWQ5dnQ3Ny9nSzBGdkZKZHFpUWV5ekhSeWhhYnBsaXFFUjMyRGRlRllXSXovck1Jck5PTEZuOXlRNUF5QnhPU1hhdFdnejVLRGdEUWRlR3FLalptTTd0N3lZRkQ3Rld0dlVTZzhLWjRhWmRSZVpRcUdldEhhS0t6SzV1RFNCMFV4TU9iakhiN2duUXI3aC8rNzMxUG9SN0hmVjBwaVBUUVlxNGk3UGJaNFNNbklRcEdKdjZKbjB6S3JPOE9ENmw3STZSNmVTOURLdHQ2YnhKTEtNNkZ6Rjh3aGdjMXpJaUwyV0RjM2hSVXVNZ3YyaXNKcksrQlc0V2dPYTdqaFhJcEwvWENPRHFoczlndldQWE1zWXdxZlVyKzQ3OEJVTmlBZ2tFWkFBQT1cIl0sXCJleHRyYUF0dHJpYnV0ZXNcIjp7XCJ3aXgtZ3ppcHBlZC1zY29wZVwiOlwiXCJ9fSIsImlhdCI6MTcxNTA4ODYyMywiZXhwIjoxNzE1MDg4OTIzfQ.ZdyPqD6YKCN1VQKuSPo3-3mS56bzBLRM1XtCAaQqk3eq7l54ZtZBiZBfpg0e8Ba1lZi2mOejI9qjRDc8kL-ve3IONQD2spfAUeC_FhdMRMA76c2dEmxda0WdMiQvKX6NDuY3ECjqJ5RyDBYGRxRVQtdtg_ByzoMdkJbVzanNFFk13c0iZLWk2CJ4kK4Gct6VjhIrr7DcVEsJrbZZaRqmab9k6Qn7QpKVb2QuBJhChzVievpgY-Ch6WqumJeJTWLivQtcy9pS1bAptszz_ScNQI-A6y51ut_w_YfmVEjQnzGuTC8B6zB9FPqttPN7EBMXtTij6s9nHJaMjMurTRKccw"
    url=f"https://www.wixapis.com/stores-reader/v1/products/{product_id}/productOptionsAvailability"
    headers = {'Authorization': access_token}
    payload = json.dumps({
    "productOptions": [
        {
            "optionType": optionType,
            "name": Name,
        }
        ]
    })

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        product_data = response.json()
        app_logger.info(f'Successfully retrieved product Availability details: {product_data}')
        return product_data 
    except requests.exceptions.RequestException as e:
        app_logger.error(f'Failed to retrieve product Availability details: {e}')
        return "Failed to retrieve product Availability details", 500


    
