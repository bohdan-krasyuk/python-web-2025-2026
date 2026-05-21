from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
if TYPE_CHECKING:
    from app.models.client_country import ClientCountry
    from app.models.client import Client


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(String(3), nullable=False, unique=True)

    client_countries: Mapped[list["ClientCountry"]] = relationship(back_populates="country")

    clients: AssociationProxy[list["Client"]] = association_proxy(
        "client_countries",
        "client",
        creator=lambda client: ClientCountry(client=client),
    )