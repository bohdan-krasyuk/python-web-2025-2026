from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models.client_country import ClientCountry
    from app.models.country import Country


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(510), nullable=False)

    client_countries: Mapped[list["ClientCountry"]] = relationship(
        back_populates="client"
    )

    countries: AssociationProxy[list["Country"]] = association_proxy(
        "client_countries",
        "country",
        creator=lambda country: ClientCountry(country=country)
    )