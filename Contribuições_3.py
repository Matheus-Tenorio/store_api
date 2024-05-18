from pydantic import BaseModel, Field
from bson import ObjectId

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    name: str
    price: float

class ProductUpdate(BaseModel):
    name: str = None
    price: float = None
