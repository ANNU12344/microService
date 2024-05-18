
from typing import List
import logging

import os
import re
import hmac
import base64
import hashlib
from flask import request, abort
from dotenv import load_dotenv
load_dotenv()
APP_ID = os.environ.get('APP_ID')
def generate_install_redirect_url(token: str):
    REDIRECT_URL="https://www.google.com/"
    redirect_url = f"https://www.wix.com/installer/install?token={token}&appId={APP_ID}&redirectUrl={REDIRECT_URL}"
    print('redirect_url', redirect_url)
    return redirect_url



