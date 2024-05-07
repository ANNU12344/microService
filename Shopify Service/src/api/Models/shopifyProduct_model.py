from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
from sqlalchemy.ext.declarative import declared_attr
from src.api.Models.baseProduct_model import BaseProduct
from datetime import datetime



class ShopifyProductImage(db.Model):
    __tablename__ = 'shopify_product_image'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('shopify_product.id'), nullable=False)
    position = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    src = db.Column(db.String(255))
    variant_ids = db.Column(db.JSON)
    
    
    @classmethod
    def from_json(cls, json_data):
        return cls(
            position=json_data.get('position'),
            created_at=cls.parse_datetime(json_data.get('created_at')),
            updated_at=cls.parse_datetime(json_data.get('updated_at')),
            width=json_data.get('width'),
            height=json_data.get('height'),
            src=json_data.get('src'),
            variant_ids=json_data.get('variant_ids', [])
        )

    @staticmethod
    def parse_datetime(datetime_str):
        if datetime_str:
            return datetime.fromisoformat(datetime_str)
        return None


class ShopifyProductVariant(db.Model):
    __tablename__ = 'shopify_product_variant'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('shopify_product.id'), nullable=False)
    barcode = db.Column(db.String(255))
    compare_at_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    fulfillment_service = db.Column(db.String(255))
    grams = db.Column(db.Integer)
    weight = db.Column(db.Float)
    weight_unit = db.Column(db.String(255))
    inventory_item_id = db.Column(db.Integer)
    inventory_management = db.Column(db.String(255))
    inventory_policy = db.Column(db.String(255))
    inventory_quantity = db.Column(db.Integer)
    option1 = db.Column(db.String(255))
    position = db.Column(db.Integer)
    price = db.Column(db.Float)
    requires_shipping = db.Column(db.Boolean)
    sku = db.Column(db.String(255))
    taxable = db.Column(db.Boolean)
    title = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime)
    
    @classmethod
    def from_json(cls, json_data):
        return cls(
            barcode=json_data.get('barcode'),
            compare_at_price=json_data.get('compare_at_price'),
            created_at=cls.parse_datetime(json_data.get('created_at')),
            fulfillment_service=json_data.get('fulfillment_service'),
            grams=json_data.get('grams'),
            weight=json_data.get('weight'),
            weight_unit=json_data.get('weight_unit'),
            inventory_item_id=json_data.get('inventory_item_id'),
            inventory_management=json_data.get('inventory_management'),
            inventory_policy=json_data.get('inventory_policy'),
            inventory_quantity=json_data.get('inventory_quantity'),
            option1=json_data.get('option1'),
            position=json_data.get('position'),
            price=json_data.get('price'),
            requires_shipping=json_data.get('requires_shipping'),
            sku=json_data.get('sku'),
            taxable=json_data.get('taxable'),
            title=json_data.get('title'),
            updated_at=cls.parse_datetime(json_data.get('updated_at'))
        )
        
    @staticmethod
    def parse_datetime(datetime_str):
        if datetime_str:
            return datetime.fromisoformat(datetime_str)
        return None
    


class ShopifyProduct(BaseProduct):
    __tablename__ = 'shopify_product'

    product_type = db.Column(db.String(255))
    published_at = db.Column(db.DateTime)
    published_scope = db.Column(db.String(255))
    status = db.Column(db.String(255))
    tags = db.Column(db.String(255))
    template_suffix = db.Column(db.String(255))
    vendor = db.Column(db.String(255))

    images = db.relationship('ShopifyProductImage', backref='product', lazy=True)
    variants = db.relationship('ShopifyProductVariant', backref='product', lazy=True)

    def serialize(self):
        base_data = super().serialize()
        shopify_data = {
            'product_type': self.product_type,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'published_scope': self.published_scope,
            'status': self.status,
            'tags': self.tags,
            'template_suffix': self.template_suffix,
            'vendor': self.vendor,
            'images': [image.serialize() for image in self.images],
            'variants': [variant.serialize() for variant in self.variants]
            # Add more Shopify-specific attributes as needed
        }
        return {**base_data, **shopify_data}
