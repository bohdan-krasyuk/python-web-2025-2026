from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, insert, update
from sqlalchemy.orm import joinedload

from app.db import DatabaseContext
from app.models import Category
from app.models.product import Product


class ProductRepository:
    def __init__(self, database_context: DatabaseContext):
        self.database_context = database_context

    def add_product(self, product_name: str, product_price: float, category_id: int) -> Product:
        # product = Product(name=product_name, price=product_price)
        #
        # self.database_context.add(product)
        # self.database_context.commit()
        #
        # return product

        query = insert(Product).values(name=product_name, price=product_price, category_id=category_id).returning(Product)
        result = self.database_context.execute(query)
        self.database_context.commit()

        return result.scalar_one()


    def update_product(self, product_id: int, product_name: str, product_price: float) -> Product:
        # product = self.database_context.query(Product).where(Product.id == product_id).one_or_none()
        # if not product:
        #     pass
        #
        # product.name = product_name
        # product.price = product_price
        #
        # self.database_context.commit()
        #
        # return product

        product_query = select(Product).where(Product.id == product_id)
        product = self.database_context.execute(product_query).scalar_one_or_none()
        if product is None:
            pass

        update_query = update(Product).values(name=product_name, price=product_price).where(Product.id == product_id).returning(Product)
        result = self.database_context.execute(update_query)
        self.database_context.commit()

        return result.scalar_one()


    def get_all(self):
        query = select(Product)
        products = self.database_context.execute(query).scalars().all()

        return products


ProductRepositoryDependency = Annotated[ProductRepository, Depends()]
