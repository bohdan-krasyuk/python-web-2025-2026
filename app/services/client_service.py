from typing import Annotated

from fastapi import Depends

from app.dtos.client_dtos import ClientDto
from app.repositories.client_repository import ClientRepositoryDependency


class ClientService:
    def __init__(self, client_repository: ClientRepositoryDependency):
        self.client_repository = client_repository

    def get_all(self):
        clients = self.client_repository.get_all()

        return [ClientDto.model_validate(c, from_attributes=True) for c in clients]


ClientServiceDependency = Annotated[ClientService, Depends()]