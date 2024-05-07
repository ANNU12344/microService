from automapper import mapper
from src.Domain.Entities.product import Product
from src.Interactor.Exception.custom_exceptions import MappingException

def product_dto(json_data):
    try:
        return mapper.to(Product).map(json_data)
    except Exception as e:
        raise MappingException(e)