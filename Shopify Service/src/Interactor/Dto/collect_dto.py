from automapper import mapper
from src.Domain.Entities.collect import Collect
from src.Interactor.Exception.custom_exceptions import MappingException

def collect_dto(json_data):
    try:
        return mapper.to(Collect).map(json_data)
    except Exception as e:
        raise MappingException(e)