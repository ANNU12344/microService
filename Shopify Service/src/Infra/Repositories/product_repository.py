from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
from src.api.Models.shopifyProduct_model import ShopifyProduct

class ShopifyProductRepository:
    def create_shopify_product(self, data):
        new_product = ShopifyProduct(**data)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def get_shopify_product_by_id(self, product_id):
        return ShopifyProduct.query.filter_by(product_id=product_id).first()

    def get_all_shopify_products(self):
        return ShopifyProduct.query.all()

    def update_shopify_product(self, product_id, data):
        product = ShopifyProduct.query.filter_by(product_id=product_id).first()
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
            return product
        return None

    def delete_shopify_product(self, product_id):
        product = ShopifyProduct.query.filter_by(product_id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
