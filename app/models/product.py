from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Float, ForeignKey

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import Category


"""
1) встановити пакет - uv add alembic
2) ініціалізувати alembic - alembic init db
3) підʼєднати класи - app/models/base.py, app/models/__init__.py
4) додати метадату - db/env.py
5) додати рядок зʼєднання з бд - alembic.ini
6) створити ревізію - alembic revision --autogenerate -m "revision name"
7) застосувати ревізію - alembic upgrade head / alembic upgrade +1
8) [optional] відкотити ревізію - alembic downgrade -1
"""

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )

    category: Mapped["Category"] = relationship(back_populates="products")
