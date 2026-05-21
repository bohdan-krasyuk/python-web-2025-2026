from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models.client import Client
    from app.models.country import Country


class ClientCountry(Base):
    __tablename__ = "client_countries"

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id", ondelete="RESTRICT"), primary_key=True
    )
    client: Mapped["Client"] = relationship(back_populates="client_countries")

    country_id: Mapped[int] = mapped_column(
        ForeignKey("countries.id", ondelete="CASCADE"), primary_key=True,
    )
    country: Mapped["Country"] = relationship(back_populates="client_countries")
