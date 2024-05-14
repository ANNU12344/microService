import os
import json
from typing import List
import logging
from flask import jsonify
import requests
from requests.exceptions import HTTPError
from dotenv import load_dotenv
load_dotenv()
APP_ID = os.environ.get('APP_ID')
APP_SECRET_KEY= os.environ.get('APP_SECRET_KEY')

REQUEST_METHODS = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DEL": requests.delete
}

class WixClientToken():

    def __init__(self,access_token: str,refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        url=f"https://www.wixapis.com/apps/v1/scripts"


    @staticmethod
    def authenticate(code: str) -> str:
        url = f"https://www.wix.com/oauth/access"
        print(APP_ID)
        payload = {
            "client_id": APP_ID,
            "client_secret": APP_SECRET_KEY,
            "grant_type": "authorization_code",
            "code": code
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return  response.json()['access_token'], response.json()['refresh_token']
        except HTTPError as ex:
            logging.exception(ex)
            return None
        


    @staticmethod
    def refresh(refresh_token:str)->str:
        url=f"https://www.wix.com/oauth/access"
        payload = {
            "app_id": APP_ID,
            "app_secret_key": APP_SECRET_KEY,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()['access_token']
        except HTTPError as ex:
            logging.exception(ex)
            return None
    

    def get_embedded_script(self):
        url=f"https://www.wixapis.com/apps/v1/scripts"
        request_func=REQUEST_METHODS['GET']
        headers = {'Authorization': self.access_token}
        try:
            response=request_func(url,headers=headers)
            response.raise_for_status()
            logging.debug(f"get_embedded_script response:\n{json.dumps(response.json(), indent=4)}")
            return response['properties']['parameters']
        except HTTPError as ex:
            logging.exception(ex)
            return None
        
    def embed_script(self,keyNmae123:str):
        url=f"https://www.wixapis.com/apps/v1/scripts"
        request_func=REQUEST_METHODS['POST']
        payload={
            "properties": {
                "parameters": {
                    "KeyName123": keyNmae123
                    }
                }
        }
        headers = {'Authorization': self.access_token}

        try:
            response=request_func(url,headers=headers,json=payload)
            response.raise_for_status()
            logging.debug(f"embed_script response:\n{json.dumps(response.json(), indent=4)}")
            return response['properties']['parameters']
        except HTTPError as ex:
            logging.exception(ex)
            return None




    
    
    