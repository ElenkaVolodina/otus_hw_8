from pydantic import BaseModel


class OrderCreate(BaseModel):
    address: str
    count: int
    hotel_id: int = None
    flight_id: int = None
    status: str = 'created'


class Order(OrderCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True
