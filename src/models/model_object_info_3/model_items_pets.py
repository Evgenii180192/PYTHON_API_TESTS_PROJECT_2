from pydantic import BaseModel, field_validator

from src.models.model_object_info_3.model_Items_dog import ItemsDog
from src.models.model_object_info_3.model_items_cat import ItemsCat


class ItemsPets(BaseModel):
    cat: ItemsCat
    dog: ItemsDog
