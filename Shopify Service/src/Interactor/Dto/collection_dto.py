from automapper import mapper
from src.Domain.Entities.collection import Collection
from src.Interactor.Exception.custom_exceptions import MappingException

def collection_dto(json_data):
    try:
        return mapper.to(Collection).map(json_data)
    except Exception as e:
        raise MappingException(e)