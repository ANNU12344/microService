from datetime import datetime


class Configuration:
    store_id: str
    businessName: str
    site_display_name: str
    platform_name: str
    platform_id: str
    auth_token: str
    is_active: bool
    created_on: datetime
    

    def __init__(self, store_id: str, businessName: str, site_display_name: str, platform_name: str, platform_id: str, auth_token: str, is_active: bool, created_on: datetime):
        self.store_id = store_id
        self.businessName = businessName
        self.site_display_name = site_display_name
        self.platform_name = platform_name
        self.platform_id = platform_id
        self.auth_token = auth_token
        self.is_active = is_active
        self.created_on = created_on



    # Json Serializer
    def serialize(self):
        return {
            'store_id': self.store_id,
            'businessName': self.businessName,
            'site_display_name': self.site_display_name,
            'platform_name': self.platform_name,
            'platform_id': self.platform_id,
            'auth_token': self.auth_token,
            'is_active': self.is_active,
            'created_on': self.created_on
         
        }