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
class WixClientToken():

    def __init__(self,access_token: str,refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token


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