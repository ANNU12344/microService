from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body_html = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    handle = db.Column(db.String(255), nullable=False, unique=True)
    product_type = db.Column(db.String(255), nullable=True)
    published_at = db.Column(db.DateTime, nullable=False)
    published_scope = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(255), nullable=True)
    template_suffix = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=False)
    vendor = db.Column(db.String(255), nullable=True)

    # One-to-Many relationship with images
    images = db.relationship('Image', backref='product', lazy=True)

    # One-to-One relationship with options
    options = db.relationship('Option', backref='product', uselist=False, lazy=True)

    # One-to-Many relationship with variants
    variants = db.relationship('Variant', backref='product', lazy=True)

class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    src = db.Column(db.String(255), nullable=True)

class Option(db.Model):
    __tablename__ = 'option'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    
    # One-to-Many relationship with option values
    values = db.relationship('OptionValue', backref='option', lazy=True)

class OptionValue(db.Model):
    __tablename__ = 'option_value'

    id = db.Column(db.Integer, primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
    value = db.Column(db.String(255), nullable=False)

class Variant(db.Model):
    __tablename__ = 'variant'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    barcode = db.Column(db.String(255), nullable=True)
    compare_at_price = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    fulfillment_service = db.Column(db.String(255), nullable=True)
    grams = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    weight_unit = db.Column(db.String(50), nullable=True)
    inventory_item_id = db.Column(db.Integer, nullable=True)
    inventory_management = db.Column(db.String(255), nullable=True)
    inventory_policy = db.Column(db.String(50), nullable=True)
    inventory_quantity = db.Column(db.Integer, nullable=True)
    option1 = db.Column(db.String(255), nullable=True)
    position = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=False)
    requires_shipping = db.Column(db.Boolean, nullable=False)
    sku = db.Column(db.String(255), nullable=True)
    taxable = db.Column(db.Boolean, nullable=False)
    title = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=False)
