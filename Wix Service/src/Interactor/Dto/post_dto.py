from automapper import mapper
from src.Domain.Entities.post import Post
from src.Interactor.Exception.custom_exceptions import MappingException

def post_dto(json_data):
    try:
        return mapper.to(Post).map(json_data)
    except Exception as e:
        raise MappingException(e)