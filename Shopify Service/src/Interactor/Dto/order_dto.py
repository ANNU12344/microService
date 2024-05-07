from automapper import mapper
from src.Domain.Entities.order import Order
from src.Interactor.Exception.custom_exceptions import MappingException

def order_dto(json_data):
    try:
        return mapper.to(Order).map(json_data)
    except Exception as e:
        raise MappingException(e)