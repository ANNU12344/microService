from typing import List, Any
from datetime import datetime


class Option:
    id: int
    product_id: int
    name: str
    position: int
    values: List[str]

    def __init__(self, id: int, product_id: int, name: str, position: int, values: List[str]) -> None:
        self.id = id
        self.product_id = product_id
        self.name = name
        self.position = position
        self.values = values

class Price:
    amount: str
    currency_code: str

    def __init__(self, amount: str, currency_code: str) -> None:
        self.amount = amount
        self.currency_code = currency_code


class PresentmentPrice:
    price: Price
    compare_at_price: None

    def __init__(self, price: Price, compare_at_price: None) -> None:
        self.price = price
        self.compare_at_price = compare_at_price


class Variant:
    id: int
    product_id: int
    title: str
    price: str
    sku: str
    position: int
    inventory_policy: str
    compare_at_price: None
    fulfillment_service: str
    inventory_management: None
    option1: str
    option2: None
    option3: None
    created_at: datetime
    updated_at: datetime
    taxable: bool
    barcode: None
    grams: int
    image_id: None
    weight: int
    weight_unit: str
    inventory_item_id: int
    inventory_quantity: int
    old_inventory_quantity: int
    presentment_prices: List[PresentmentPrice]
    requires_shipping: bool
    admin_graphql_api_id: str

    def __init__(self, id: int, product_id: int, title: str, price: str, sku: str, position: int, inventory_policy: str, compare_at_price: None, fulfillment_service: str, inventory_management: None, option1: str, option2: None, option3: None, created_at: datetime, updated_at: datetime, taxable: bool, barcode: None, grams: int, image_id: None, weight: int, weight_unit: str, inventory_item_id: int, inventory_quantity: int, old_inventory_quantity: int, presentment_prices: List[PresentmentPrice], requires_shipping: bool, admin_graphql_api_id: str) -> None:
        self.id = id
        self.product_id = product_id
        self.title = title
        self.price = price
        self.sku = sku
        self.position = position
        self.inventory_policy = inventory_policy
        self.compare_at_price = compare_at_price
        self.fulfillment_service = fulfillment_service
        self.inventory_management = inventory_management
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.created_at = created_at
        self.updated_at = updated_at
        self.taxable = taxable
        self.barcode = barcode
        self.grams = grams
        self.image_id = image_id
        self.weight = weight
        self.weight_unit = weight_unit
        self.inventory_item_id = inventory_item_id
        self.inventory_quantity = inventory_quantity
        self.old_inventory_quantity = old_inventory_quantity
        self.presentment_prices = presentment_prices
        self.requires_shipping = requires_shipping
        self.admin_graphql_api_id = admin_graphql_api_id


class Product:
    id: int
    title: str
    body_html: str
    vendor: str
    product_type: str
    created_at: datetime
    handle: str
    updated_at: datetime
    published_at: None
    template_suffix: None
    published_scope: str
    tags: str
    status: str
    admin_graphql_api_id: str
    variants: List[Variant]
    options: List[Option]
    images: List[Any]
    image: None

    def __init__(self, id: int, title: str, body_html: str, vendor: str, product_type: str, created_at: datetime, handle: str, updated_at: datetime, published_at: None, template_suffix: None, published_scope: str, tags: str, status: str, admin_graphql_api_id: str, variants: List[Variant], options: List[Option], images: List[Any], image: None) -> None:
        self.id = id
        self.title = title
        self.body_html = body_html
        self.vendor = vendor
        self.product_type = product_type
        self.created_at = created_at
        self.handle = handle
        self.updated_at = updated_at
        self.published_at = published_at
        self.template_suffix = template_suffix
        self.published_scope = published_scope
        self.tags = tags
        self.status = status
        self.admin_graphql_api_id = admin_graphql_api_id
        self.variants = variants
        self.options = options
        self.images = images
        self.image = image

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body_html": self.body_html,
            "vendor": self.vendor,
            "product_type": self.product_type,
            "created_at": self.created_at,
            "handle": self.handle,
            "updated_at": self.updated_at,
            "published_at": self.published_at,
            "template_suffix": self.template_suffix,
            "published_scope": self.published_scope,
            "tags": self.tags,
            "status": self.status,
            "admin_graphql_api_id": self.admin_graphql_api_id,
            "variants": self.variants,
            "options": self.options,
            "images": self.images,
            "image": self.image
        }
