from typing import Annotated

from fastapi import Depends

from app.dtos.product_dtos import ProductDto, NewProductCreateDto, UpdateProductDto
from app.models.product import Product
from app.repositories.product_repository import ProductRepositoryDependency


class ProductService:
    def __init__(self, repository: ProductRepositoryDependency):
        self.repository = repository

    def get_all_for_public(self):
        products = self.repository.get_all()

        return [ProductDto.model_validate(p, from_attributes=True) for p in products]

    def create(self, product_dto: ProductDto):
        new_products = self.repository.add_product(product_dto.name, product_dto.price, product_dto.category_id)

        return NewProductCreateDto.model_validate(new_products, from_attributes=True)

    def update(self, product_dto: UpdateProductDto):
        updated_products = self.repository.update_product(product_dto.id, product_dto.name, product_dto.price)

        return UpdateProductDto.model_validate(updated_products, from_attributes=True)


ProductServiceDependency = Annotated[ProductService, Depends()]