from datetime import datetime

class StoreUser:
    first_name: str
    last_name: str
    email: str
    password: str
    active: bool
    activation_code: str
    store_id: int
    created_on: datetime
    last_login_time: datetime
    app_id: str
    platform_id: str
    
    def __init__(self, first_name: str, last_name: str, email: str, password: str, active: bool, activation_code: str, store_id: int, created_on: datetime, last_login_time: datetime, app_id: str, platform_id: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active
        self.activation_code = activation_code
        self.store_id = store_id
        self.created_on = created_on
        self.last_login_time = last_login_time
        self.app_id = app_id
        self.platform_id = platform_id

    # Json Serializer
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'active': self.active,
            'activation_code': self.activation_code,
            'store_id': self.store_id,
            'created_on': self.created_on,
            'last_login_time': self.last_login_time,
            'app_id': self.app_id,
            'platform_id': self.platform_id
        }
