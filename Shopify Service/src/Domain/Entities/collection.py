from datetime import datetime
from typing import Optional, List


class Image:
    created_at: datetime
    alt: str
    width: int
    height: int
    src: str

    def __init__(self, created_at: datetime, alt: str, width: int, height: int, src: str) -> None:
        self.created_at = created_at
        self.alt = alt
        self.width = width
        self.height = height
        self.src = src


class Collection:
    id: int
    handle: str
    title: str
    updated_at: datetime
    body_html: str
    published_at: datetime
    sort_order: str
    template_suffix: None
    published_scope: str
    admin_graphql_api_id: str
    image: Optional[Image]

    def __init__(self, id: int, handle: str, title: str, updated_at: datetime, body_html: str, published_at: datetime, sort_order: str, template_suffix: None, published_scope: str, admin_graphql_api_id: str, image: Optional[Image] = None) -> None:
        self.id = id
        self.handle = handle
        self.title = title
        self.updated_at = updated_at
        self.body_html = body_html
        self.published_at = published_at
        self.sort_order = sort_order
        self.template_suffix = template_suffix
        self.published_scope = published_scope
        self.admin_graphql_api_id = admin_graphql_api_id
        self.image = image
