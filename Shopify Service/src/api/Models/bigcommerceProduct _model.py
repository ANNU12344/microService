from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
from sqlalchemy.ext.declarative import declared_attr
from src.api.Models.baseProduct_model import BaseProduct


class BigcommerceProductImage(db.Model):
    __tablename__ = 'bigcommerce_product_image'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('bigcommerce_product.id'), nullable=False)
    image_file = db.Column(db.String(255))
    is_thumbnail = db.Column(db.Boolean)
    sort_order = db.Column(db.Integer)
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    date_modified = db.Column(db.DateTime)

class BigcommerceProductVideo(db.Model):
    __tablename__ = 'bigcommerce_product_video'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('bigcommerce_product.id'), nullable=False)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    sort_order = db.Column(db.Integer)
    type = db.Column(db.String(255))
    video_id = db.Column(db.String(255))
    length = db.Column(db.String(255))

class BigcommerceProductVariant(db.Model):
    __tablename__ = 'bigcommerce_product_variant'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('bigcommerce_product.id'), nullable=False)
    cost_price = db.Column(db.Float)
    price = db.Column(db.Float)
    sale_price = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    weight = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)
    depth = db.Column(db.Float)
    is_free_shipping = db.Column(db.Boolean)
    fixed_cost_shipping_price = db.Column(db.Float)
    purchasing_disabled = db.Column(db.Boolean)
    purchasing_disabled_message = db.Column(db.String(255))
    upc = db.Column(db.String(255))
    inventory_level = db.Column(db.BigInteger)
    inventory_warning_level = db.Column(db.BigInteger)
    bin_picking_number = db.Column(db.String(255))
    mpn = db.Column(db.String(255))
    gtin = db.Column(db.String(255))
    option_values = db.Column(db.JSON)
    calculated_price = db.Column(db.Float)
    calculated_weight = db.Column(db.Float)

class BigcommerceProductOption(db.Model):
    __tablename__ = 'bigcommerce_product_option'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('bigcommerce_product.id'), nullable=False)
    display_name = db.Column(db.String(255))
    type = db.Column(db.String(255))
    config = db.Column(db.JSON)
    sort_order = db.Column(db.Integer)
    option_values = db.relationship('BigcommerceProductOptionValue', backref='option', lazy=True)

class BigcommerceProductOptionValue(db.Model):
    __tablename__ = 'bigcommerce_product_option_value'

    id = db.Column(db.Integer, primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('bigcommerce_product_option.id'), nullable=False)
    is_default = db.Column(db.Boolean)
    label = db.Column(db.String(255))
    sort_order = db.Column(db.Integer)
    value_data = db.Column(db.JSON)

class BigcommerceProductModifier(db.Model):
    __tablename__ = 'bigcommerce_product_modifier'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('bigcommerce_product.id'), nullable=False)
    type = db.Column(db.String(255))
    required = db.Column(db.Boolean)
    sort_order = db.Column(db.Integer)
    config = db.Column(db.JSON)
    display_name = db.Column(db.String(255))
    name = db.Column(db.String(255))
    option_values = db.relationship('BigcommerceProductOptionValue', backref='modifier', lazy=True)

class BigcommerceProduct(BaseProduct):
    __tablename__ = 'bigcommerce_product'

    brand_id = db.Column(db.BigInteger)
    brand_name = db.Column(db.String(255))
    inventory_tracking = db.Column(db.String(255))
    fixed_cost_shipping_price = db.Column(db.Float)
    is_free_shipping = db.Column(db.Boolean)
    is_visible = db.Column(db.Boolean)
    is_featured = db.Column(db.Boolean)
    related_products = db.Column(db.JSON)
    warranty = db.Column(db.String(255))
    bin_picking_number = db.Column(db.String(255))
    layout_file = db.Column(db.String(255))
    upc = db.Column(db.String(255))
    search_keywords = db.Column(db.String(255))
    availability_description = db.Column(db.String(255))
    availability = db.Column(db.String(255))
    gift_wrapping_options_type = db.Column(db.String(255))
    gift_wrapping_options_list = db.Column(db.JSON)
    sort_order = db.Column(db.Integer)
    condition = db.Column(db.String(255))
    is_condition_shown = db.Column(db.Boolean)
    order_quantity_minimum = db.Column(db.BigInteger)
    order_quantity_maximum = db.Column(db.BigInteger)
    page_title = db.Column(db.String(255))
    meta_keywords = db.Column(db.JSON)
    meta_description = db.Column(db.String(255))
    view_count = db.Column(db.BigInteger)
    preorder_release_date = db.Column(db.DateTime)
    preorder_message = db.Column(db.String(255))
    is_preorder_only = db.Column(db.Boolean)
    is_price_hidden = db.Column(db.Boolean)
    price_hidden_label = db.Column(db.String(255))
    custom_url = db.Column(db.JSON)
    open_graph_type = db.Column(db.String(255))
    open_graph_title = db.Column(db.String(255))
    open_graph_description = db.Column(db.String(255))
    open_graph_use_meta_description = db.Column(db.Boolean)
    open_graph_use_product_name = db.Column(db.Boolean)
    open_graph_use_image = db.Column(db.Boolean)
    gtin = db.Column(db.String(255))
    mpn = db.Column(db.String(255))
    reviews_rating_sum = db.Column(db.Integer)
    reviews_count = db.Column(db.Integer)
    total_sold = db.Column(db.BigInteger)
    custom_fields = db.Column(db.JSON)
    bulk_pricing_rules = db.Column(db.JSON)
    images = db.relationship('BigcommerceProductImage', backref='product', lazy=True)
    videos = db.relationship('BigcommerceProductVideo', backref='product', lazy=True)
    variants = db.relationship('BigcommerceProductVariant', backref='product', lazy=True)
    options = db.relationship('BigcommerceProductOption', backref='product', lazy=True)
    modifiers = db.relationship('BigcommerceProductModifier', backref='product', lazy=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    base_variant_id = db.Column(db.BigInteger)
    calculated_price = db.Column(db.Float)
    option_set_id = db.Column(db.Integer)
    option_set_display = db.Column(db.String(255))

    def serialize(self):
        base_data = super().serialize()
        bigcommerce_data = {
            'brand_id': self.brand_id,
            'brand_name': self.brand_name,
            'inventory_tracking': self.inventory_tracking,
            'fixed_cost_shipping_price': self.fixed_cost_shipping_price,
            'is_free_shipping': self.is_free_shipping,
            'is_visible': self.is_visible,
            'is_featured': self.is_featured,
            'related_products': self.related_products,
            'warranty': self.warranty,
            'bin_picking_number': self.bin_picking_number,
            'layout_file': self.layout_file,
            'upc': self.upc,
            'search_keywords': self.search_keywords,
            'availability_description': self.availability_description,
            'availability': self.availability,
            'gift_wrapping_options_type': self.gift_wrapping_options_type,
            'gift_wrapping_options_list': self.gift_wrapping_options_list,
            'sort_order': self.sort_order,
            'condition': self.condition,
            'is_condition_shown': self.is_condition_shown,
            'order_quantity_minimum': self.order_quantity_minimum,
            'order_quantity_maximum': self.order_quantity_maximum,
            'page_title': self.page_title,
            'meta_keywords': self.meta_keywords,
            'meta_description': self.meta_description,
            'view_count': self.view_count,
            'preorder_release_date': self.preorder_release_date.isoformat() if self.preorder_release_date else None,
            'preorder_message': self.preorder_message,
            'is_preorder_only': self.is_preorder_only,
            'is_price_hidden': self.is_price_hidden,
            'price_hidden_label': self.price_hidden_label,
            'custom_url': self.custom_url,
            'open_graph_type': self.open_graph_type,
            'open_graph_title': self.open_graph_title,
            'open_graph_description': self.open_graph_description,
            'open_graph_use_meta_description': self.open_graph_use_meta_description,
            'open_graph_use_product_name': self.open_graph_use_product_name,
            'open_graph_use_image': self.open_graph_use_image,
            'gtin': self.gtin,
            'mpn': self.mpn,
            'reviews_rating_sum': self.reviews_rating_sum,
            'reviews_count': self.reviews_count,
            'total_sold': self.total_sold,
            'custom_fields': self.custom_fields,
            'bulk_pricing_rules': self.bulk_pricing_rules,
            'images': [image.serialize() for image in self.images],
            'videos': [video.serialize() for video in self.videos],
            'variants': [variant.serialize() for variant in self.variants],
            'options': [option.serialize() for option in self.options],
            'modifiers': [modifier.serialize() for modifier in self.modifiers],
            'date_created': self.date_created.isoformat() if self.date_created else None,
            'date_modified': self.date_modified.isoformat() if self.date_modified else None,
            'base_variant_id': self.base_variant_id,
            'calculated_price': self.calculated_price,
            'option_set_id': self.option_set_id,
            'option_set_display': self.option_set_display
            # Add more Bigcommerce-specific attributes as needed
        }
        return {**base_data, **bigcommerce_data}
