from pydantic import BaseModel

class CountryDto(BaseModel):
    name: str

class ClientCountryDto(BaseModel):
    country: CountryDto

class ClientDto(BaseModel):
    full_name: str
    #client_countries: list[ClientCountryDto]
    countries: list[CountryDto]