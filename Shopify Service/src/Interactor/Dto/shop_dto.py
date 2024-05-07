from automapper import mapper
from src.Domain.Entities.shop import Shop
from src.Interactor.Exception.custom_exceptions import MappingException


def shop_dto(json_data):
    try:
        return mapper.to(Shop).map(json_data)
    except Exception as e:
        raise MappingException(e)