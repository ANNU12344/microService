from datetime import datetime

class Uninstall:
    store_id: int
    store_name: str
    platform_id: str
    platform_name: str
    
    def __init__(self, store_id: int, store_name: str, platform_id: str, platform_name: str) -> None:
        self.store_id = store_id
        self.store_name = store_name
        self.platform_id = platform_id
        self.platform_name = platform_name

    # Json Serializer
    def serialize(self):
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'platform_id': self.platform_id,
            'platform_name': self.platform_name
        }
