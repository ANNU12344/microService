import jwt
from functools import wraps
from flask import request, jsonify
from src.Domain.Constant.constant import JWT_SECRET_KEY
from src.Interactor.Logger.custom_logger import app_logger



def jwt_authentication(JWT_SECRET_KEY):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            
            print(f'JWT Token: {token}')

            if not token:
                return jsonify({'message': 'Missing token'}), 401

            try:
                decoded_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'], issuer='Computelib', audience='EcomApplicationPlatformUsers')
                app_logger.info(f'Decoded JWT Payload: {decoded_payload}')
            except jwt.ExpiredSignatureError:
                print("Token has expired.")
                app_logger.error("Token has expired.")
                return jsonify({'message': 'Token has expired'})
            except jwt.InvalidTokenError as e:
                print(f"Invalid token: {e}")
                return jsonify({'message': 'Invalid token'})

            return f(*args, **kwargs)

        return decorated
    return decorator


jwt_wrapper = jwt_authentication(JWT_SECRET_KEY)