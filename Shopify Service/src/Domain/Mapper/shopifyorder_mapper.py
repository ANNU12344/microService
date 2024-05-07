from automapper import mapper
from src.Domain.Entities.order import Order
from src.Interactor.Exception.custom_exceptions import MappingException

def map_json_to_shop(json_data):
    try:
        return mapper.to(Order).map(json_data)
    except Exception as e:
        raise MappingException(e)