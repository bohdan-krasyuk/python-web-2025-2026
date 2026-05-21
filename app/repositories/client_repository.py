from typing import Annotated

from fastapi import Depends
from sqlalchemy import select

from app.db import DatabaseContext
from app.models import Client


class ClientRepository:
    def __init__(self, database_context: DatabaseContext):
        self.database_context = database_context

    def get_all(self):
        query = select(Client)

        return self.database_context.execute(query).scalars().all()


ClientRepositoryDependency = Annotated[ClientRepository, Depends()]