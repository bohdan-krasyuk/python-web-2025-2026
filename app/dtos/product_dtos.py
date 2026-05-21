from pydantic import BaseModel, Field


class CategoryDto(BaseModel):
    id: int
    name: str
    short_name: str

# dto - Data Transfer Object
class ProductDto(BaseModel):
    name: str = Field(min_length=3, max_length=255, description="Name of the product") # len(name) - x, x > min_length
    price: float = Field(gt=0, description="Price of the product") # gt - greater than >, ge - greater or equal >=
    category_id: int = Field(gt=0, description="Category id of the product")
    category: CategoryDto | None = Field(description="Category of the product", default=None)
    # price: PositiveFloat


class NewProductCreateDto(ProductDto):
    id: int

class UpdateProductDto(ProductDto):
    id: int