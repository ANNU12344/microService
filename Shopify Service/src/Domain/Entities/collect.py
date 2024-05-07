from datetime import datetime


class Collect:
    collection_id: int
    created_at: datetime
    id: int
    position: int
    product_id: int
    sort_value: str
    updated_at: datetime

    def __init__(self, collection_id: int, created_at: datetime, id: int, position: int, product_id: int, sort_value: str, updated_at: datetime) -> None:
        self.collection_id = collection_id
        self.created_at = created_at
        self.id = id
        self.position = position
        self.product_id = product_id
        self.sort_value = sort_value
        self.updated_at = updated_at
