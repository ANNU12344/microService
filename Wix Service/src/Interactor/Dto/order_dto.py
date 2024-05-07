from src.Domain.Entities.order import Order
from automapper import mapper
def order_dto(json_data):
    return mapper.to(Order).map(json_data)
    