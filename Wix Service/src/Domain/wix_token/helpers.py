from functools import wraps
import logging
import os
from flask import request, abort
from dotenv import load_dotenv
load_dotenv()
APP_ID = os.environ.get('APP_ID')
def generate_install_redirect_url(token: str):
    REDIRECT_URL="https://www.google.com/"
    redirect_url = f"https://www.wix.com/installer/install?token={token}&appId={APP_ID}&redirectUrl={REDIRECT_URL}"
    print('redirect_url', redirect_url)
    return redirect_url


def verify_web_call(f):
    @wraps(f)
    def wrapper(*args, **kwargs) -> bool:
        get_args = request.args

        code = get_args.get('code')
        if not code:
            logging.error(f"Code not found")
            abort(401)

        wix_site=get_args.get('wix_site')
        if not wix_site:
            logging.error(f"Wix Site not recieved: {wix_site}")
            abort(401)
        return f(*args, **kwargs)
    return wrapper


