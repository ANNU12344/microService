from datetime import datetime


class Configuration:
    store_configuration_json: str
    store_id: int
    email: str
    store_name: str
    platform_name: str
    platform_id: str
    auth_token: str
    is_active: bool
    created_on: datetime
    store_ui_configuration_json: str

    def __init__(self, store_configuration_json: str, store_id: int, email: str, store_name: str, platform_name: str, platform_id: str, auth_token: str, is_active: bool,  created_on: datetime, store_ui_configuration_json: str) -> None:
        self.store_configuration_json = store_configuration_json
        self.store_id = store_id
        self.email = email
        self.store_name = store_name
        self.platform_name = platform_name
        self.platform_id = platform_id
        self.auth_token = auth_token
        self.is_active = is_active
        self.created_on = created_on
        self.store_ui_configuration_json = store_ui_configuration_json


    # Json Serializer
    def serialize(self):
        return {
            'store_configuration_json': self.store_configuration_json,
            'store_id': self.store_id,
            'email': self.email,
            'store_name': self.store_name,
            'platform_name': self.platform_name,
            'platform_id': self.platform_id,
            'auth_token': self.auth_token,
            'is_active': self.is_active,
            'created_on': self.created_on,
            'store_ui_configuration_json': self.store_ui_configuration_json
        }