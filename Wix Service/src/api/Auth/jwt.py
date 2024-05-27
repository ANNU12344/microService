from flask import Flask
import sys
import jwt
import json
from functools import wraps
from flask import request, jsonify
from src.Domain.Constant.constant import APP_PUBLIC_KEY
from src.Interactor.Logger.custom_logger import app_logger



def jwt_authentication(APP_PUBLIC_KEY):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # token contain oauth2. as prefix
            token_with_prefix = request.headers.get('Authorization')
            token = token_with_prefix.split('OAUTH2.')[1]
            parts = token.split('.')
            if len(parts) != 3:
                print("Invalid token format")
            print(f'JWT Token: {token}')

            if not token:
                return jsonify({'message': 'Missing token'}), 401

            try:
                decoded_payload = jwt.decode(request.data, APP_PUBLIC_KEY, algorithms=["RS256"])
                app_logger.info(f'Decoded JWT Payload: {decoded_payload}')
            except Exception as err:
                print(f"Invalid error: {err}")
                return jsonify({'message': 'Invalid token'})

        return decorated
    return decorator


jwt_wrapper = jwt_authentication(APP_PUBLIC_KEY=APP_PUBLIC_KEY)