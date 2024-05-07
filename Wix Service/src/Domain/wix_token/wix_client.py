import os
import json
from typing import List
import logging
from flask import jsonify
import requests
from requests.exceptions import HTTPError

from dotenv import load_dotenv

load_dotenv()

WIX_APP_ID = os.environ.get('APP_ID')
WIX_SECRET_KEY = os.environ.get('App_SECRET_KEY')
class WixClientToken():

    def __init__(self,access_token: str,refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token


    @staticmethod
    def authenticate(code: str) -> str:
        url = f"https://www.wix.com/oauth/access"
        payload = {
            "client_id": "59eebad7-ad17-4315-a97e-3d5f6521f410",
            "client_secret": "db3a0e7a-26c5-4f48-bc83-532aa533bc12",
            "grant_type": "authorization_code",
            "code": code
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()['access_token']
        except HTTPError as ex:
            logging.exception(ex)
            return None
        

    @staticmethod
    def refresh(refresh:str)->str:
        url=f"https://www.wix.com/oauth/access"
        payload = {
            "app_id": "59eebad7-ad17-4315-a97e-3d5f6521f410",
            "app_secret_key": "db3a0e7a-26c5-4f48-bc83-532aa533bc12",
            "grant_type": "refresh_token",
            "refresh_token": refresh
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()['access_token']
        except HTTPError as ex:
            logging.exception(ex)
            return None